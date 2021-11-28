# 🔗 domain-trails 
````shell
  -------------------------------------------------------------------------------
      ____                            _           ______              _  __     
     / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
    / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
   / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  ) 
  /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/  
  -------------------------------------------------------------------------------
    Domain Trails - domains footprints, reconnaissance & information gathering   
  -------------------------------------------------------------------------------
````
Starting a simple project around information gathering related to domain / url / web addresses. This project is intended
for educational means, so what is in this project right now ...

Currently, project is running on native python 3.6 with no external dependency. I will be working on collecting
information by analyzing domain, web pages and online sources. Project is supporting followings

`⚠️This tool is educational. Don't use it to abuse the online services & servers. If there is any query and question 
please open an issue.`  



## ✨ Highlighting

### Console Output

- Supported `-d ` param at the moment for single domain name input.

#### Registered Domain Information

````commandline
python domain-trails/portal.py -d www.cnn.com
Printing Results for domain www.cnn.com

Domain Availability Result for www.cnn.com : Domain is Registered

DNS History Records
Old Web Host     New Web Host     Month / Year     Zone Date        Transaction      
---------------  ---------------  ---------------  ---------------  ---------------  
ultradns.org     n/a              february 2017    2017-03-01       removed          
ultradns.net     n/a              february 2017    2017-03-01       removed          
ultradns.info    n/a              february 2017    2017-03-01       removed          
ultradns.co.uk   n/a              february 2017    2017-03-01       removed          
n/a              ultradns.org     november 2016    2016-12-01       added            
n/a              ultradns.net     november 2016    2016-12-01       added            
n/a              ultradns.info    november 2016    2016-12-01       added            
n/a              ultradns.co.uk   november 2016    2016-12-01       added            
timewarner.net   awsdns-11.co.uk  september 2016   2016-10-01       transfer         
timewarner.net   awsdns-08.net    september 2016   2016-10-01       transfer         
timewarner.net   awsdns-07.org    september 2016   2016-10-01       transfer         
timewarner.net   awsdns-05.com    september 2016   2016-10-01       transfer         
dynect.net       awsdns-11.co.uk  september 2016   2016-10-01       transfer         
dynect.net       awsdns-08.net    september 2016   2016-10-01       transfer         
dynect.net       awsdns-07.org    september 2016   2016-10-01       transfer         
dynect.net       awsdns-05.com    september 2016   2016-10-01       transfer         
n/a              dynect.net       november 2012    2012-12-01       added            
aol.com          timewarner.net   february 2010    2010-03-01       transfer         
ans.net          aol.com          march 2002       2002-04-01       transfer         
ans.net          n/a              december 2000                     epoch    
````

#### Deleted & Available Domain Information

````commandline
python domain-trails/portal.py -d www.iteamdevelopers.org
Printing Results for domain www.iteamdevelopers.org

Domain Availability Result for www.iteamdevelopers.org : domain available

DNS History Records
Old Web Host       New Web Host       Month / Year       Zone Date          Transaction        
-----------------  -----------------  -----------------  -----------------  -----------------  
foundationapi.com  n/a                december 2017      2018-01-01         deleted            
cloudflare.com     foundationapi.com  november 2017      2017-12-01         transfer           
foundationapi.com  cloudflare.com     december 2015      2016-01-01         transfer           
cloudflare.com     foundationapi.com  november 2015      2015-12-01         transfer           
freehosting.com    cloudflare.com     january 2015       2015-02-01         transfer           
foundationapi.com  freehosting.com    december 2014      2015-01-01         transfer           
freehosting.com    foundationapi.com  november 2014      2014-12-01         transfer           
creative-tech.org  freehosting.com    may 2014           2014-06-01         transfer           
serversfree.com    creative-tech.org  november 2013      2013-12-01         transfer           
000webhost.com     serversfree.com    july 2013          2013-08-01         transfer           
n/a                000webhost.com     november 2012      2012-12-01         new    
````

### 🙋 Domain Availability Check

You can use following function to check if domain is available or not

````python
from core.recon.domain_available import DomainAvailable as DomainTest

dt_object = DomainTest("www.yourdomain.com")
print(dt_object.domain_available)
````

Its output is boolean `True` or `False`.

### 📜 Domain History Check

You can use following function to check domain's previous host history

````python
from core.recon.dns_history import DnsHistory as DomainHistory

dt_object = DomainHistory("www.github.com")
print(dt_object.domain_history)
````

Its output is json example following `Reduced output`
````json
[
  {
    "old_web_host": "dynect.net",
    "new_web_host": "n/a",
    "month_year": "july 2020",
    "zone_date": "2020-08-01",
    "transaction": "removed"
  },
  {
    "old_web_host": "n/a",
    "new_web_host": "jsn-server2.com",
    "month_year": "january 2006",
    "zone_date": "2006-02-01",
    "transaction": "new"
  },
  {
    "old_web_host": "n/a",
    "new_web_host": "jsn-server5.com",
    "month_year": "january 2006",
    "zone_date": "2006-02-01",
    "transaction": "new"
  }
]

````

### 🚧 Learning, searching, coding and hunting in progress ... 