# pip install Sublist3r

import sublist3r
import socket
import logging
from time import time
import requests
import statistics
import threading

scan_port_list = [21, 22, 23, 53, 80, 443, *range(8000, 8010)]
tries_for_latency_check = 5
connect_timeout = 2


def get_country(ip_adr: str):
    response = requests.get(f"https://ipinfo.io/{ip_adr}/json", verify = True)
    # print(response.json())
    if response.status_code != 200:
        return None
    return f"{response.json()['country']}, {response.json()['region']}, {response.json()['city']}"


def measure_tcp_connect_latency_ms(host: str, port: int = 443, timeout: int = 5) -> float:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s_start = time()
    try:
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)
    except socket.timeout:
        # logging.log(logging.WARNING, f"Timeout while connect to {host}:{port}")
        return None
    except:
        # logging.log(logging.WARNING, f"Unable connect to {host}:{port}")
        return None
    s_runtime = (time() - s_start) * 1000
    return float(s_runtime)


class MultiScan:
    def __init__(self, subdomains):
        self.subdomains = subdomains
        self.lock = None

    def subdomain_scan(self, domain):
        response_text = ''
        response_text += f"\nDomain: {domain}"
        try:
            domain_ips = socket.gethostbyname_ex(domain)[2]
            for ip in domain_ips:
                response_text += f"\n\tIP address: {ip}"
                tcp_latencies = []
                errors = 0
                opened_ports = []
                for port in scan_port_list:
                    tcp_latency = measure_tcp_connect_latency_ms(ip, port=port, timeout=connect_timeout)
                    if tcp_latency:
                        opened_ports.append(port)
                        tcp_latencies.append(tcp_latency)
                        if len(tcp_latencies)+errors < tries_for_latency_check:
                            for i in range(tries_for_latency_check):
                                tcp_latency = measure_tcp_connect_latency_ms(ip, port=port, timeout=connect_timeout)
                                if tcp_latency is None:
                                    errors += 1
                                else:
                                    tcp_latencies.append(tcp_latency)
                country = get_country(ip)
                if country:
                    response_text += f"\n\t\tCountry: {country}"
                if len(tcp_latencies):
                    response_text += f"\n\t\tTCP connection to {ip} min/max/mean : {round(min(tcp_latencies),2)}/" \
                          f"{round(max(tcp_latencies),2)}/" \
                          f"{round(statistics.mean(tcp_latencies),2)} ms. " \
                          f"Sent {(len(tcp_latencies)+errors)}, " \
                          f"received {len(tcp_latencies)} " \
                          f"({float(errors)*100/(len(tcp_latencies)+errors)}% errors)"
                    response_text += f"\n\t\tOpen tcp ports: {', '.join(map(str, opened_ports))}"
        except socket.gaierror:
            logging.log(logging.WARNING, f"Unable to resolve {domain}")
        print(response_text)

    def run(self):
        self.lock = threading.BoundedSemaphore(value=scan_threads)
        for subdomain in self.subdomains:
            t = threading.Thread(target=self.subdomain_scan, args=(subdomain,))
            t.start()


scan_threads = 30
if __name__ == '__main__':
    subdomains = sublist3r.main("exness.com",
                                threads=scan_threads,
                                savefile=None,
                                ports=None,
                                silent=True,
                                verbose=False,
                                enable_bruteforce=False,
                                engines=None)
    scanner = MultiScan(subdomains)
    scanner.run()
