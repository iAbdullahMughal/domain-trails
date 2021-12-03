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

`⚠️This tool is for educational propuse only. Don't use it to abuse the online services & servers. `

Starting a simple project around information gathering related to domain / url / web addresses. This project is intended
for educational means, so what is in this project right now ...

## ✨ Highlights
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

Read Docs 

- https://readthedocs.org/projects/domain-trails/
- https://iabdullahmughal.github.io/domain-trails/


Following services are supported

- ☑️ Domain Availability Check
- 📜 Domain Hosting History (based on dns)
- 📇️Domain DNS Information


Work in progress 
- 🔄 Whois information (include history)
- 🔄 Web Technologies
- 🔄 Information over internet

## 📋 Output
Following console output
````commandline
$ portal.py -d www.king.com
-------------------------------------------------------------------------------
      ____                            _           ______              _  __     
     / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
    / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
   / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  ) 
  /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/  
  -------------------------------------------------------------------------------
    Domain Trails - domains footprints, reconnaissance & information gathering 
  -------------------------------------------------------------------------------
Printing Results for domain www.king.com

Domain Availability Result for www.king.com : Domain is Registered

DNS History Records
Old Web Host       New Web Host       Month / Year    Zone Date   Transaction  
-----------------  -----------------  --------------  ----------  -----------  
fjordnetwork.com   ultradns.co.uk     october 2006    2006-11-01  transfer     
midasplayer.com    ultradns.org       october 2006    2006-11-01  transfer     
midasplayer.com    ultradns.net       october 2006    2006-11-01  transfer     
midasplayer.com    ultradns.info      october 2006    2006-11-01  transfer     
midasplayer.com    ultradns.co.uk     october 2006    2006-11-01  transfer     
fjordnetwork.com   ultradns.org       october 2006    2006-11-01  transfer     
fjordnetwork.com   ultradns.net       october 2006    2006-11-01  transfer     
fjordnetwork.com   ultradns.info      october 2006    2006-11-01  transfer     
name-services.com  fjordnetwork.com   november 2005   2005-12-01  transfer     
name-services.com  midasplayer.com    november 2005   2005-12-01  transfer     
register.com       name-services.com  september 2005  2005-10-01  transfer     
register.com       n/a                december 2000               epoch        

Parent Name Server records
name       type  class  ttl  endpoint        
---------  ----  -----  ---  --------------  
king.com.  A     IN     60   34.120.128.178  

Mail eXchanger (MX) Records
name       type  class  ttl    endpoint                            
---------  ----  -----  -----  ----------------------------------  
king.com.  MX    IN     86253  20 mxb-0017bd02.gslb.pphosted.com.  
king.com.  MX    IN     86253  10 mxa-0017bd02.gslb.pphosted.com.  

Local Name Server Records
name       type  class  ttl    endpoint               
---------  ----  -----  -----  ---------------------  
king.com.  NS    IN     86253  pdns1.ultradns.net.    
king.com.  NS    IN     86253  pdns2.ultradns.net.    
king.com.  NS    IN     86253  pdns3.ultradns.org.    
king.com.  NS    IN     86253  pdns4.ultradns.org.    
king.com.  NS    IN     86253  pdns5.ultradns.info.   
king.com.  NS    IN     86253  pdns6.ultradns.co.uk.  

Start of Authority (SOA)
primary_nameserver     host_master_email         serial_number  refresh  retry  expire   minimum_ttl  
---------------------  ------------------------  -------------  -------  -----  -------  -----------  
dns1.midasplayer.com.  servers.midasplayer.com.  2021112500     86400    1800   3600000  1800         

Text Records
name       type  class  ttl    endpoint                                                                                                                              
---------  ----  -----  -----  ------------------------------------------------------------------------------------------------------------------------------------  
king.com.  TXT   IN     86254  MS=ms45280793                                                                                                                         
king.com.  TXT   IN     86254  ZOOM_verify_tm9sSAVUTH6xPjBMX4KpaA                                                                                                    
king.com.  TXT   IN     86254  docusign=92c8b0d4-c137-4dd8-8332-5eeac333574b                                                                                         
king.com.  TXT   IN     86254  docusign=ed5a6125-f2a5-4e56-a651-a66b674b2495                                                                                         
king.com.  TXT   IN     86254  adobe-sign-verification=dcb38d595da1afe98c9538c4f8322efd                                                                              
king.com.  TXT   IN     86254  onetrust-domain-verification=ae1052dabbe14c24bd0622dca8f7c1b9                                                                         
king.com.  TXT   IN     86254  google-site-verification=AUquS5ouChge7fx5mACCTb2_AaQfxAH5erWM5M-qQxE                                                                  
king.com.  TXT   IN     86254  google-site-verification=FXhQoNsSX64v9A-zAvTL_ZuAckOddcdWbwOEd349azQ                                                                  
king.com.  TXT   IN     86254  google-site-verification=Wj0IdA4K6g1Ghrdon8vcp82Pb0wIwHQVfunNeTyT4d4                                                                  
king.com.  TXT   IN     86254  google-site-verification=Zz-ZafS5SB2fjCqho7OGI7eYK7AGmWbuI92Uto088zo                                                                  
king.com.  TXT   IN     86254  "google-site-verification=YADvET1Vko-f_BnkjiWdPIyUKmZqcaUPn8w8_v299uQ "                                                               
king.com.  TXT   IN     86254  BDBKf8jWD+g/SMrTglIMgqxdzwyjehK9mtXuJnnEqfMt97/+c+bS8gDlPwudHi1z1lhyMbdCbAMN+va3k3peLw==                                              
king.com.  TXT   IN     86254  cisco-ci-domain-verification=7857d8bc0ecd25bc6c708e3a913b0eaed1cef529f406e5472235051a93638db6                                         
king.com.  TXT   IN     86254  atlassian-domain-verification=zgWQpzQViZLGaYL2GIW7hKWpr6aAZhVzDaB9pQMftfYI28JPsael2eX5QpXXJxIn                                        
king.com.  TXT   IN     86254  "v=spf1 include:spf1.king.com include:spf2.king.com mx include:u8225371.wl122.sendgrid.net include:u7865735.wl236.sendgrid.net ~all"  

````

## Documentation


### 🚧 Learning, searching, coding and hunting in progress ... 