## Сканер поддоменов ресурса exness.com 
### Установка зависимостей и запуск:
```
pip3 install Sublist3r
git clone https://github.com/ruslan337/exness_scan.git
cd exness_scan
python3 main.py
```
### Конфиги
Начало файлов main.py содержит следующие переменне, которые можно менять
```
scan_port_list = [22, 80, 443]  # Порты по которым мы устанавливаем tcp соединение
tries_for_latency_check = 5     # -c из ping (гарантий нет, может и больше отправить, лень было break и if писать)
connect_timeout = 2             # -W из ping
```
### Результат сканирования из Алматы:
```
Domain: www.exness.com
	IP address: 15.184.243.160
		Country: BH, Manama, Manama
		TCP connection to 15.184.243.160 min/max/mean : 297.59/327.58/311.72 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 15.184.157.197
		Country: BH, Manama, Manama
		TCP connection to 15.184.157.197 min/max/mean : 218.11/408.29/283.5 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: 120.exness.com
WARNING:root:Unable to resolve 120.exness.com

Domain: admin.exness.com
	IP address: 45.60.15.25
		Country: US, California, Redwood City
		TCP connection to 45.60.15.25 min/max/mean : 89.62/103.42/96.9 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.admin.exness.com

Domain: ads.exness.com
WARNING:root:Unable to resolve www.admin.exness.com
WARNING:root:Unable to resolve ads.exness.com

Domain: algw-proxy.exness.com
	IP address: 103.6.128.118
		Country: HK, Central and Western, Hong Kong
		TCP connection to 103.6.128.118 min/max/mean : 235.13/317.13/293.3 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.algw-proxy.exness.com
WARNING:root:Unable to resolve www.algw-proxy.exness.com

Domain: amazon-dsn-processor.exness.com
	IP address: 45.60.15.25
		Country: US, California, Redwood City
		TCP connection to 45.60.15.25 min/max/mean : 86.9/101.52/95.19 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.amazon-dsn-processor.exness.com
WARNING:root:Unable to resolve www.amazon-dsn-processor.exness.com

Domain: api.exness.com
	IP address: 45.60.15.25
		Country: US, California, Redwood City
		TCP connection to 45.60.15.25 min/max/mean : 88.69/106.29/98.32 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.api.exness.com
WARNING:root:Unable to resolve www.api.exness.com
WARNING:root:Unable to resolve backoffice.exness.com
WARNING:root:Unable to resolve www.backoffice.exness.com

Domain: backoffice.exness.com

Domain: www.backoffice.exness.com

Domain: beatbot.exness.com
WARNING:root:Unable to resolve beatbot.exness.com

Domain: www.beatbot.exness.com

Domain: beta.exness.com
WARNING:root:Unable to resolve www.beatbot.exness.com
WARNING:root:Unable to resolve beta.exness.com
WARNING:root:Unable to resolve www.beta.exness.com

Domain: www.beta.exness.com

Domain: blog.exness.com
	IP address: 13.251.232.145
		Country: SG, Singapore, Singapore
		TCP connection to 13.251.232.145 min/max/mean : 255.07/341.92/297.18 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.blog.exness.com
WARNING:root:Unable to resolve www.blog.exness.com

Domain: bonus-stats.exness.com
WARNING:root:Unable to resolve bonus-stats.exness.com

Domain: calendar.exness.com
	IP address: 64.233.161.121
		Country: FI, Uusimaa, Helsinki
		TCP connection to 64.233.161.121 min/max/mean : 76.04/199.52/99.89 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.calendar.exness.com

Domain: campaign.exness.com
WARNING:root:Unable to resolve www.calendar.exness.com
	IP address: 3.126.202.50
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 3.126.202.50 min/max/mean : 100.66/215.72/132.24 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 3.69.136.55
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 3.69.136.55 min/max/mean : 99.13/172.66/113.25 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.campaign.exness.com

Domain: chat-mapper.exness.com
WARNING:root:Unable to resolve www.campaign.exness.com
	IP address: 107.154.196.37
		Country: HK, Central and Western, Hong Kong
		TCP connection to 107.154.196.37 min/max/mean : 370.96/474.02/403.29 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.chat-mapper.exness.com

Domain: cup.exness.com
WARNING:root:Unable to resolve www.chat-mapper.exness.com
	IP address: 103.6.128.118
		Country: HK, Central and Western, Hong Kong
		TCP connection to 103.6.128.118 min/max/mean : 239.06/339.31/277.2 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.cup.exness.com
WARNING:root:Unable to resolve www.cup.exness.com

Domain: d1656.exness.com
WARNING:root:Unable to resolve d1656.exness.com
WARNING:root:Unable to resolve www.d1656.exness.com

Domain: www.d1656.exness.com

Domain: deposit.exness.com
	IP address: 45.60.81.118
		Country: US, California, Redwood City
		TCP connection to 45.60.81.118 min/max/mean : 90.66/104.48/96.1 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.deposit.exness.com
WARNING:root:Unable to resolve www.deposit.exness.com

Domain: dev3.exness.com
WARNING:root:Unable to resolve dev3.exness.com

Domain: directory.exness.com

Domain: www.directory.exness.com

Domain: directory-ext.exness.com
WARNING:root:Unable to resolve directory.exness.com
WARNING:root:Unable to resolve www.directory.exness.com
	IP address: 107.154.50.46
		Country: US, California, Redwood City
		TCP connection to 107.154.50.46 min/max/mean : 104.5/183.85/130.33 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.directory-ext.exness.com
WARNING:root:Unable to resolve www.directory-ext.exness.com

Domain: djadmin.exness.com

Domain: www.djadmin.exness.com
WARNING:root:Unable to resolve djadmin.exness.com
WARNING:root:Unable to resolve www.djadmin.exness.com

Domain: education.exness.com
	IP address: 104.199.255.176
		Country: TW, Taiwan, Taipei
		TCP connection to 104.199.255.176 min/max/mean : 345.34/458.34/387.25 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.education.exness.com
WARNING:root:Unable to resolve www.education.exness.com

Domain: education-stage.exness.com
	IP address: 45.60.81.64
		Country: US, California, Redwood City
		TCP connection to 45.60.81.64 min/max/mean : 92.34/102.57/97.27 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.education-stage.exness.com

Domain: email.exness.com
WARNING:root:Unable to resolve www.education-stage.exness.com

Domain: erp.exness.com
WARNING:root:Unable to resolve email.exness.com

Domain: errors.exness.com
WARNING:root:Unable to resolve erp.exness.com
	IP address: 54.254.153.41
		Country: SG, Singapore, Singapore
		TCP connection to 54.254.153.41 min/max/mean : 245.9/383.22/272.64 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 52.77.71.169
		Country: SG, Singapore, Singapore
		TCP connection to 52.77.71.169 min/max/mean : 251.95/328.25/273.38 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: ex.exness.com

Domain: fxnews.exness.com
WARNING:root:Unable to resolve ex.exness.com
	IP address: 143.198.65.220
		Country: US, California, Santa Clara
		TCP connection to 143.198.65.220 min/max/mean : 228.34/309.42/266.55 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.fxnews.exness.com
WARNING:root:Unable to resolve www.fxnews.exness.com

Domain: geo-cn.exness.com
	IP address: 15.184.243.160
		Country: BH, Manama, Manama
		TCP connection to 15.184.243.160 min/max/mean : 216.47/319.33/246.72 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 15.184.157.197
		Country: BH, Manama, Manama
		TCP connection to 15.184.157.197 min/max/mean : 217.27/309.84/258.8 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.geo-cn.exness.com
WARNING:root:Unable to resolve www.geo-cn.exness.com

Domain: geo-uk.exness.com
	IP address: 15.184.157.197
		Country: BH, Manama, Manama
		TCP connection to 15.184.157.197 min/max/mean : 210.72/657.14/305.6 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 15.184.243.160
		Country: BH, Manama, Manama
		TCP connection to 15.184.243.160 min/max/mean : 216.21/309.82/276.96 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.geo-uk.exness.com
WARNING:root:Unable to resolve www.geo-uk.exness.com

Domain: click.global.exness.com
WARNING:root:Unable to resolve click.global.exness.com

Domain: cloud.global.exness.com
WARNING:root:Unable to resolve cloud.global.exness.com

Domain: image.global.exness.com
WARNING:root:Unable to resolve image.global.exness.com

Domain: view.global.exness.com
WARNING:root:Unable to resolve view.global.exness.com

Domain: ha3.exness.com
WARNING:root:Unable to resolve ha3.exness.com

Domain: help.exness.com
	IP address: 13.251.232.145
		Country: SG, Singapore, Singapore
		TCP connection to 13.251.232.145 min/max/mean : 253.06/360.79/270.05 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.help.exness.com
WARNING:root:Unable to resolve www.help.exness.com

Domain: hubspot-forms.exness.com
WARNING:root:Unable to resolve hubspot-forms.exness.com
WARNING:root:Unable to resolve www.hubspot-forms.exness.com

Domain: www.hubspot-forms.exness.com

Domain: internal.exness.com
WARNING:root:Unable to resolve internal.exness.com

Domain: www.internal.exness.com
WARNING:root:Unable to resolve www.internal.exness.com

Domain: ldap-node01.exness.com

Domain: www.ldap-node01.exness.com

Domain: ldap-node02.exness.com
WARNING:root:Unable to resolve ldap-node01.exness.com
WARNING:root:Unable to resolve www.ldap-node01.exness.com

Domain: www.ldap-node02.exness.com

Domain: level2.exness.com
WARNING:root:Unable to resolve ldap-node02.exness.com
WARNING:root:Unable to resolve www.ldap-node02.exness.com
WARNING:root:Unable to resolve level2.exness.com
WARNING:root:Unable to resolve www.level2.exness.com

Domain: www.level2.exness.com

Domain: level3.exness.com
	IP address: 107.154.50.46
		Country: US, California, Redwood City
		TCP connection to 107.154.50.46 min/max/mean : 102.53/105.88/104.24 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.level3.exness.com
WARNING:root:Unable to resolve www.level3.exness.com

Domain: links.exness.com
WARNING:root:Unable to resolve links.exness.com

Domain: mail.exness.com
	IP address: 193.194.119.187
		Country: NL, North Holland, Amsterdam
	IP address: 193.194.119.186
		Country: NL, North Holland, Amsterdam

Domain: mail-01.exness.com
	IP address: 193.194.119.186
		Country: NL, North Holland, Amsterdam

Domain: mail-02.exness.com
	IP address: 193.194.119.187
		Country: NL, North Holland, Amsterdam

Domain: mail-03.exness.com
	IP address: 193.194.119.188
		Country: NL, North Holland, Amsterdam

Domain: mail-04.exness.com
	IP address: 193.194.119.189
		Country: NL, North Holland, Amsterdam

Domain: mail-05.exness.com
	IP address: 193.194.119.185
		Country: NL, North Holland, Amsterdam

Domain: mail-06.exness.com

Domain: marketing.exness.com
WARNING:root:Unable to resolve mail-06.exness.com
	IP address: 3.126.202.50
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 3.126.202.50 min/max/mean : 97.83/107.1/102.05 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 3.69.136.55
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 3.69.136.55 min/max/mean : 93.76/103.63/99.76 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: member.exness.com

Domain: www.member.exness.com

Domain: msg.exness.com
WARNING:root:Unable to resolve member.exness.com
WARNING:root:Unable to resolve www.member.exness.com

Domain: mt4real11.exness.com
WARNING:root:Unable to resolve msg.exness.com
	IP address: 107.154.50.97
		Country: US, California, Redwood City

Domain: mt4real4.exness.com
	IP address: 107.154.50.72
		Country: US, California, Redwood City

Domain: mt4trial2.exness.com
	IP address: 188.42.227.175
		Country: NL, North Holland, Amsterdam

Domain: mt5trial.exness.com
	IP address: 213.196.50.4
		Country: NL, North Holland, Amsterdam

Domain: mtrt.exness.com
WARNING:root:Unable to resolve mtrt.exness.com
WARNING:root:Unable to resolve www.mtrt.exness.com

Domain: www.mtrt.exness.com

Domain: my.exness.com
	IP address: 45.60.81.64
		Country: US, California, Redwood City
		TCP connection to 45.60.81.64 min/max/mean : 90.41/105.03/97.24 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.my.exness.com

Domain: mypartner.exness.com
WARNING:root:Unable to resolve www.my.exness.com
	IP address: 45.60.78.64
		Country: US, California, Redwood City
		TCP connection to 45.60.78.64 min/max/mean : 78.02/86.0/81.8 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.mypartner.exness.com

Domain: n2ws.exness.com
WARNING:root:Unable to resolve www.mypartner.exness.com
	IP address: 35.159.15.16
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 35.159.15.16 min/max/mean : 100.36/102.7/101.36 ms. Sent 6, received 6 (0.0% errors)
		Open tcp ports: 22

Domain: www.n2ws.exness.com
WARNING:root:Unable to resolve www.n2ws.exness.com

Domain: ng2.exness.com

Domain: www.ng2.exness.com

Domain: npw-acs-asia-slb1.exness.com
WARNING:root:Unable to resolve ng2.exness.com
WARNING:root:Unable to resolve www.ng2.exness.com
	IP address: 47.57.145.2
		Country: HK, Central and Western, Hong Kong
		TCP connection to 47.57.145.2 min/max/mean : 328.23/393.53/353.59 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: ns2.exness.com

Domain: office-secure.exness.com
WARNING:root:Unable to resolve ns2.exness.com
WARNING:root:Unable to resolve office-secure.exness.com

Domain: online.exness.com

Domain: only-the-best.exness.com
WARNING:root:Unable to resolve online.exness.com
WARNING:root:Unable to resolve only-the-best.exness.com

Domain: origin.exness.com
	IP address: 188.72.207.153
		Country: NL, North Holland, Amsterdam
	IP address: 193.194.119.114
		Country: NL, North Holland, Amsterdam

Domain: partner.exness.com
	IP address: 45.60.78.64
		Country: US, California, Redwood City
		TCP connection to 45.60.78.64 min/max/mean : 74.57/87.73/81.17 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.partner.exness.com
WARNING:root:Unable to resolve www.partner.exness.com

Domain: support.partner.exness.com
WARNING:root:Unable to resolve support.partner.exness.com
WARNING:root:Unable to resolve www.support.partner.exness.com

Domain: www.support.partner.exness.com

Domain: payments.exness.com

Domain: www.payments.exness.com

Domain: static.payments.exness.com

Domain: payments-callback.exness.com
WARNING:root:Unable to resolve payments.exness.com
WARNING:root:Unable to resolve www.payments.exness.com
WARNING:root:Unable to resolve static.payments.exness.com
	IP address: 45.60.15.25
		Country: US, California, Redwood City
		TCP connection to 45.60.15.25 min/max/mean : 88.53/272.86/107.45 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.payments-callback.exness.com
WARNING:root:Unable to resolve www.payments-callback.exness.com

Domain: pga.exness.com

Domain: www.pga.exness.com

Domain: premier.exness.com
WARNING:root:Unable to resolve pga.exness.com
WARNING:root:Unable to resolve www.pga.exness.com
	IP address: 45.60.78.64
		Country: US, California, Redwood City
		TCP connection to 45.60.78.64 min/max/mean : 74.53/260.85/129.97 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.premier.exness.com

Domain: premier-stage.exness.com
WARNING:root:Unable to resolve www.premier.exness.com
	IP address: 107.154.196.37
		Country: HK, Central and Western, Hong Kong
		TCP connection to 107.154.196.37 min/max/mean : 382.08/510.82/418.74 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.premier-stage.exness.com
WARNING:root:Unable to resolve www.premier-stage.exness.com

Domain: promo.exness.com
	IP address: 13.251.232.145
		Country: SG, Singapore, Singapore
		TCP connection to 13.251.232.145 min/max/mean : 255.27/367.47/315.74 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.promo.exness.com
WARNING:root:Unable to resolve www.promo.exness.com

Domain: promotion.exness.com
	IP address: 3.69.136.55
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 3.69.136.55 min/max/mean : 96.33/107.48/100.14 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 3.126.202.50
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 3.126.202.50 min/max/mean : 100.81/106.27/103.14 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: quotes.exness.com
	IP address: 107.154.50.46
		Country: US, California, Redwood City
		TCP connection to 107.154.50.46 min/max/mean : 101.37/124.05/106.59 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.quotes.exness.com
WARNING:root:Unable to resolve www.quotes.exness.com

Domain: recon.exness.com
WARNING:root:Unable to resolve recon.exness.com
WARNING:root:Unable to resolve www.recon.exness.com

Domain: www.recon.exness.com

Domain: relay.exness.com
	IP address: 193.194.119.187
		Country: NL, North Holland, Amsterdam
	IP address: 193.194.119.186
		Country: NL, North Holland, Amsterdam

Domain: reports.exness.com
WARNING:root:Unable to resolve reports.exness.com
WARNING:root:Unable to resolve www.reports.exness.com

Domain: www.reports.exness.com

Domain: s6.exness.com

Domain: secure.exness.com
WARNING:root:Unable to resolve s6.exness.com
WARNING:root:Unable to resolve secure.exness.com

Domain: www.secure.exness.com

Domain: sentry.exness.com
WARNING:root:Unable to resolve www.secure.exness.com
WARNING:root:Unable to resolve sentry.exness.com

Domain: sf.exness.com
	IP address: 193.194.119.189
		Country: NL, North Holland, Amsterdam
	IP address: 193.194.119.188
		Country: NL, North Holland, Amsterdam

Domain: sf-magic.exness.com
	IP address: 45.60.15.25
		Country: US, California, Redwood City
		TCP connection to 45.60.15.25 min/max/mean : 89.32/345.02/111.3 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.sf-magic.exness.com
WARNING:root:Unable to resolve www.sf-magic.exness.com

Domain: smon.exness.com
	IP address: 35.158.67.203
		Country: DE, Hesse, Frankfurt am Main

Domain: www.smon.exness.com
WARNING:root:Unable to resolve www.smon.exness.com

Domain: smtp.exness.com
	IP address: 193.194.119.185
		Country: NL, North Holland, Amsterdam
	IP address: 193.194.119.189
		Country: NL, North Holland, Amsterdam
	IP address: 193.194.119.188
		Country: NL, North Holland, Amsterdam

Domain: social-trading.exness.com
	IP address: 45.60.81.64
		Country: US, California, Redwood City
		TCP connection to 45.60.81.64 min/max/mean : 92.74/111.24/100.04 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.social-trading.exness.com

Domain: a.social-trading.exness.com
WARNING:root:Unable to resolve www.social-trading.exness.com

Domain: track.social-trading.exness.com
WARNING:root:Unable to resolve a.social-trading.exness.com
	IP address: 18.163.95.44
		Country: HK, Central and Western, Hong Kong
		TCP connection to 18.163.95.44 min/max/mean : 192.58/229.17/205.2 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 16.162.194.81
		Country: HK, Central and Western, Hong Kong
		TCP connection to 16.162.194.81 min/max/mean : 192.45/267.59/213.0 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 16.162.38.172
		Country: HK, Central and Western, Hong Kong
		TCP connection to 16.162.38.172 min/max/mean : 192.43/291.03/214.89 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: stage.exness.com
	IP address: 45.60.81.64
		Country: US, California, Redwood City
		TCP connection to 45.60.81.64 min/max/mean : 88.78/102.23/96.12 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.stage.exness.com
WARNING:root:Unable to resolve www.stage.exness.com

Domain: static.exness.com
	IP address: 107.154.196.37
		Country: HK, Central and Western, Hong Kong
		TCP connection to 107.154.196.37 min/max/mean : 379.55/510.61/420.64 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: www.static.exness.com

Domain: svn.exness.com
WARNING:root:Unable to resolve www.static.exness.com

Domain: www.svn.exness.com

Domain: thaipaygw.exness.com
WARNING:root:Unable to resolve svn.exness.com
WARNING:root:Unable to resolve www.svn.exness.com

Domain: www.thaipaygw.exness.com

Domain: ticks.exness.com
WARNING:root:Unable to resolve thaipaygw.exness.com
WARNING:root:Unable to resolve www.thaipaygw.exness.com
	IP address: 193.194.119.190
		Country: NL, North Holland, Amsterdam
		TCP connection to 193.194.119.190 min/max/mean : 97.32/271.24/146.06 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.ticks.exness.com
WARNING:root:Unable to resolve www.ticks.exness.com

Domain: track.exness.com
	IP address: 18.163.95.44
		Country: HK, Central and Western, Hong Kong
		TCP connection to 18.163.95.44 min/max/mean : 190.55/307.07/244.85 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 16.162.38.172
		Country: HK, Central and Western, Hong Kong
		TCP connection to 16.162.38.172 min/max/mean : 183.31/306.73/224.8 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 16.162.194.81
		Country: HK, Central and Western, Hong Kong
		TCP connection to 16.162.194.81 min/max/mean : 205.5/312.26/291.83 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: vdfl.exness.com
	IP address: 193.194.119.135
		Country: NL, North Holland, Amsterdam
		TCP connection to 193.194.119.135 min/max/mean : 97.84/208.24/119.66 ms. Sent 6, received 6 (0.0% errors)
		Open tcp ports: 443

Domain: www.vdfl.exness.com
WARNING:root:Unable to resolve www.vdfl.exness.com

Domain: vpn.exness.com
	IP address: 193.194.117.18
		Country: GB, England, Twyford
		TCP connection to 193.194.117.18 min/max/mean : 107.37/193.17/142.57 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 193.194.119.132
		Country: NL, North Holland, Amsterdam
		TCP connection to 193.194.119.132 min/max/mean : 99.01/180.58/118.66 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.vpn.exness.com
WARNING:root:Unable to resolve www.vpn.exness.com

Domain: vpn-01.exness.com
	IP address: 193.194.119.132
		Country: NL, North Holland, Amsterdam
		TCP connection to 193.194.119.132 min/max/mean : 98.09/180.71/121.83 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.vpn-01.exness.com

Domain: vpn-02.exness.com
WARNING:root:Unable to resolve www.vpn-01.exness.com
	IP address: 193.194.117.18
		Country: GB, England, Twyford
		TCP connection to 193.194.117.18 min/max/mean : 105.58/200.37/135.55 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.vpn-02.exness.com
WARNING:root:Unable to resolve www.vpn-02.exness.com

Domain: vpn-03.exness.com
WARNING:root:Unable to resolve vpn-03.exness.com

Domain: vpn-hk.exness.com
	IP address: 103.6.128.119
		Country: HK, Central and Western, Hong Kong
		TCP connection to 103.6.128.119 min/max/mean : 231.18/339.9/277.42 ms. Sent 6, received 6 (0.0% errors)
		Open tcp ports: 443

Domain: www.vpn-hk.exness.com
WARNING:root:Unable to resolve www.vpn-hk.exness.com

Domain: vpn-nl.exness.com
	IP address: 193.194.119.131
		Country: NL, North Holland, Amsterdam
		TCP connection to 193.194.119.131 min/max/mean : 99.35/196.86/126.58 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www.vpn-nl.exness.com
WARNING:root:Unable to resolve www.vpn-nl.exness.com

Domain: vpn2-nl.exness.com

Domain: webinars.exness.com
WARNING:root:Unable to resolve vpn2-nl.exness.com

Domain: webmoney.exness.com
WARNING:root:Unable to resolve webinars.exness.com
WARNING:root:Unable to resolve webmoney.exness.com

Domain: webtrader.exness.com
WARNING:root:Unable to resolve webtrader.exness.com

Domain: wl-demo.exness.com

Domain: www.wl-demo.exness.com

Domain: wox.exness.com
WARNING:root:Unable to resolve wl-demo.exness.com
WARNING:root:Unable to resolve www.wl-demo.exness.com

Domain: my.wta.exness.com
WARNING:root:Unable to resolve wox.exness.com
	IP address: 18.158.95.101
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 18.158.95.101 min/max/mean : 96.3/102.33/99.66 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 35.157.150.67
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 35.157.150.67 min/max/mean : 94.75/105.92/100.38 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443
	IP address: 52.29.35.212
		Country: DE, Hesse, Frankfurt am Main
		TCP connection to 52.29.35.212 min/max/mean : 200.31/353.36/226.4 ms. Sent 7, received 7 (0.0% errors)
		Open tcp ports: 80, 443

Domain: www66.exness.com

Domain: www.www66.exness.com
WARNING:root:Unable to resolve www66.exness.com

Domain: zabbix-sms.exness.com
WARNING:root:Unable to resolve www.www66.exness.com

Domain: www.zabbix-sms.exness.com
WARNING:root:Unable to resolve zabbix-sms.exness.com

Domain: premiumexness.com
WARNING:root:Unable to resolve www.zabbix-sms.exness.com
	IP address: 107.154.216.37
		Country: US, California, Redwood City
		TCP connection to 107.154.216.37 min/max/mean : 58.52/289.37/91.95 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009
	IP address: 107.154.192.37
		Country: US, California, Redwood City
		TCP connection to 107.154.192.37 min/max/mean : 74.84/86.54/80.77 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: theexness.com
	IP address: 107.154.192.37
		Country: US, California, Redwood City
		TCP connection to 107.154.192.37 min/max/mean : 78.3/1235.26/241.76 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009
	IP address: 107.154.216.37
		Country: US, California, Redwood City
		TCP connection to 107.154.216.37 min/max/mean : 57.72/78.54/64.52 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009

Domain: vipexness.com
	IP address: 107.154.216.37
		Country: US, California, Redwood City
	IP address: 107.154.192.37
		Country: US, California, Redwood City
		TCP connection to 107.154.192.37 min/max/mean : 79.3/333.67/171.88 ms. Sent 18, received 18 (0.0% errors)
		Open tcp ports: 53, 80, 443, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009
```
