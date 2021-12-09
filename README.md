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

### Work completed

Following services are supported

- ☑️ Domain Availability Check
- 📜 Domain Hosting History (based on dns)
- 📇️Domain DNS Information
- 🔍 Whois information (fetch whois history `if available`)

### Work in progress

- 🔄 Web Technologies (in progress)
- 🔄 Information over internet

## 🔽 Download and Install

The recommended way to download and install/update the latest stable release of oletools is to use pip:

- On Linux/Mac: ``sudo -H pip install -U domain-trails``
- On Windows: ``pip install -U domain-trails``

## 📋 Output

Following console output -

````shell
$ portal.py -d www.cnn.com
-------------------------------------------------------------------------------
      ____                            _           ______              _  __     
     / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
    / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
   / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  ) 
  /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/  
  -------------------------------------------------------------------------------
    Domain Trails - domains footprints, reconnaissance & information gathering 
  -------------------------------------------------------------------------------
Printing Results for domain www.cnn.com

Domain Availability Result for www.cnn.com : Domain is Registered


DNS History Records

Old Web Host  New Web Host  Month / Year  Zone Date  Transaction  
--------------------------  --------------------------  --------------------------  -----------------------  -------------------------  
ultradns.org                n/a                         february 2017               2017-03-01               removed                    
ultradns.net                n/a                         february 2017               2017-03-01               removed                    
ultradns.info               n/a                         february 2017               2017-03-01               removed                    
ultradns.co.uk              n/a                         february 2017               2017-03-01               removed                    
n/a                         ultradns.org                november 2016               2016-12-01               added                      
n/a                         ultradns.net                november 2016               2016-12-01               added                      
n/a                         ultradns.info               november 2016               2016-12-01               added                      
n/a                         ultradns.co.uk              november 2016               2016-12-01               added                      
timewarner.net              awsdns-11.co.uk             september 2016              2016-10-01               transfer                   
timewarner.net              awsdns-08.net               september 2016              2016-10-01               transfer                   
timewarner.net              awsdns-07.org               september 2016              2016-10-01               transfer                   
timewarner.net              awsdns-05.com               september 2016              2016-10-01               transfer                   
dynect.net                  awsdns-11.co.uk             september 2016              2016-10-01               transfer                   
dynect.net                  awsdns-08.net               september 2016              2016-10-01               transfer                   
dynect.net                  awsdns-07.org               september 2016              2016-10-01               transfer                   
dynect.net                  awsdns-05.com               september 2016              2016-10-01               transfer                   
n/a                         dynect.net                  november 2012               2012-12-01               added                      
aol.com                     timewarner.net              february 2010               2010-03-01               transfer                   
ans.net                     aol.com                     march 2002                  2002-04-01               transfer                   
ans.net                     n/a                         december 2000                                        epoch                      

Printing DNS Records Related To Domain


Parent Name Server records

name      type  class  ttl  endpoint        
--------  ----  -----  ---  --------------  
cnn.com.  A     IN     60   151.101.129.67  
cnn.com.  A     IN     60   151.101.1.67    
cnn.com.  A     IN     60   151.101.65.67   
cnn.com.  A     IN     60   151.101.193.67  

IP v6 Records

name      type  class  ttl  endpoint            
--------  ----  -----  ---  ------------------  
cnn.com.  AAAA  IN     300  2a04:4e42:600::323  
cnn.com.  AAAA  IN     300  2a04:4e42:400::323  
cnn.com.  AAAA  IN     300  2a04:4e42:200::323  
cnn.com.  AAAA  IN     300  2a04:4e42::323      

Local Name Server Records

name      type  class  ttl   endpoint                  
--------  ----  -----  ----  ------------------------  
cnn.com.  NS    IN     3600  ns-1086.awsdns-07.org.    
cnn.com.  NS    IN     3600  ns-1630.awsdns-11.co.uk.  
cnn.com.  NS    IN     3600  ns-47.awsdns-05.com.      
cnn.com.  NS    IN     3600  ns-576.awsdns-08.net.     

Mail eXchanger (MX) Records

name      type  class  ttl  endpoint                            
--------  ----  -----  ---  ----------------------------------  
cnn.com.  MX    IN     300  10 mxa-00241e02.gslb.pphosted.com.  
cnn.com.  MX    IN     300  10 mxb-00241e02.gslb.pphosted.com.  

Text Records

name      type  class  ttl  endpoint                                                                                                                  
--------  ----  -----  ---  ------------------------------------------------------------------------------------------------------------------------  
cnn.com.  TXT   IN     300  126953328-4422040                                                                                                         
cnn.com.  TXT   IN     300  133461244-4422058                                                                                                         
cnn.com.  TXT   IN     300  178953534-4422001                                                                                                         
cnn.com.  TXT   IN     300  186844776-4422028                                                                                                         
cnn.com.  TXT   IN     300  228426766-4422034                                                                                                         
cnn.com.  TXT   IN     300  267933795-4422004                                                                                                         
cnn.com.  TXT   IN     300  287893558-4422013                                                                                                         
cnn.com.  TXT   IN     300  294913881-4422049                                                                                                         
cnn.com.  TXT   IN     300  299762315-4422055                                                                                                         
cnn.com.  TXT   IN     300  2baPGrmeo+RwsWdIdq/gIVSEWNb4tC9mLGQu0j4l/mduqhm06T+V9vNLXsauLyH9FwMZJSRHvj/YHGKOVWRylw==                                  
cnn.com.  TXT   IN     300  321159687-4422031                                                                                                         
cnn.com.  TXT   IN     300  349997471-4422043                                                                                                         
cnn.com.  TXT   IN     300  353665828-4422052                                                                                                         
cnn.com.  TXT   IN     300  528183251-4422019                                                                                                         
cnn.com.  TXT   IN     300  553992719-4400647                                                                                                         
cnn.com.  TXT   IN     300  598362927-4422061                                                                                                         
cnn.com.  TXT   IN     300  667921863-4422007                                                                                                         
cnn.com.  TXT   IN     300  688162515-4422037                                                                                                         
cnn.com.  TXT   IN     300  691244352-4422022                                                                                                         
cnn.com.  TXT   IN     300  714321471-4421998                                                                                                         
cnn.com.  TXT   IN     300  754516718-4422064                                                                                                         
cnn.com.  TXT   IN     300  755973593-4422016                                                                                                         
cnn.com.  TXT   IN     300  764482256-4422025                                                                                                         
cnn.com.  TXT   IN     300  782989862-4417942                                                                                                         
cnn.com.  TXT   IN     300  826218936-4422046                                                                                                         
cnn.com.  TXT   IN     300  882269757-4422010                                                                                                         
cnn.com.  TXT   IN     300  MS=ms66433104                                                                                                             
cnn.com.  TXT   IN     300  _globalsign-domain-verification=-lBuNJDFRxDkLkNbYOLBU03PlWjnPqAzBPAVUokhAw                                                
cnn.com.  TXT   IN     300  _globalsign-domain-verification=2lybn8Z2GKCTHNehPEREKdz_jh5SahShpwOeRqCWjl                                                
cnn.com.  TXT   IN     300  _globalsign-domain-verification=5ckEJ4VIhQ6weCdCfmfzQPVP6ED1LtCX9jw1OKX5Mv                                                
cnn.com.  TXT   IN     300  _globalsign-domain-verification=B57sRQpmte4G4w-gavZbVNmmNsMxGp5kcL19UP2599                                                
cnn.com.  TXT   IN     300  _globalsign-domain-verification=MK_ZKmss4D_DdzGOsssHxxBOK6hJc6LGycFvNOESdZ                                                
cnn.com.  TXT   IN     300  _globalsign-domain-verification=S6DssfjyL_2kgK4I2Ae_1cdPfwqRRBfB9-3ZhRGMRj                                                
cnn.com.  TXT   IN     300  _globalsign-domain-verification=yTw3T3KnyIyTB1xG2GvVhl1zWJlFp-WqmNskdVI_65                                                
cnn.com.  TXT   IN     300  adobe-idp-site-verification=279ead95-3581-42b7-82f4-73c97f8cebfa                                                          
cnn.com.  TXT   IN     300  adobe-sign-verification=c3dc3217f76deddcb413a23e4e665fad                                                                  
cnn.com.  TXT   IN     300  cisco-ci-domain-verification=4a1c92ef69fe42f8125c3ca9ce0696dcf6cc16fa80243257de578af593d19548                             
cnn.com.  TXT   IN     300  d1xTs9+kADZZSz3bPphLpkMXXxBGjqn5vsQHhi2M6lo0r8AdIbm6j8LfQXPujsywVgeGSP+AXWX0vO9Iep5cUg==                                  
cnn.com.  TXT   IN     300  facebook-domain-verification=xszi21kow2trmw3xt3ph6s631zyu3i                                                               
cnn.com.  TXT   IN     300  globalsign-domain-verification=-Q7umwx2mj164XwLa0PsoUaWe2HBhta50GjggsT98f                                                 
cnn.com.  TXT   IN     300  globalsign-domain-verification=2lI5pahhCu_jg_2RC5GEdolQmAa4K7rhP7_OA-lZBK                                                 
cnn.com.  TXT   IN     300  google-site-verification=R-Btow3Z8oU_9H1IWU4Gm4lvUQ_OVmsfxonIKhIaiPE                                                      
cnn.com.  TXT   IN     300  google-site-verification=_QivaXNjhXy-V1y_YqrycXdAWZi2mVrcwbXerX6THeY                                                      
cnn.com.  TXT   IN     300  mixpanel-domain-verify=612e2914-a7fb-4965-95d5-19acc02797df                                                               
cnn.com.  TXT   IN     300  mongodb-site-verification=mtrxHeW3jOzWtwEwnOLpeQo9NXh6Lqas                                                                
cnn.com.  TXT   IN     300  ms=ms97284866                                                                                                             
cnn.com.  TXT   IN     300  stripe-verification=094254c9a60a6dc0c1c2a62294b81c0c3b9363d044151a3e562ffeac0a7c4157                                      
cnn.com.  TXT   IN     300  stripe-verification=5535d8a3c7b3517ee3765df8bd66b8a5cf70a65c3437f5be5d3a8f0108b790ef                                      
cnn.com.  TXT   IN     300  "v=spf1 include:cnn.com._nspf.vali.email include:%{i}._ip.%{h}._ehlo.%{d}._spf.vali.email include:mail.zendesk.com ~all"  

Start of Authority (SOA)

primary_nameserver    host_master_email              serial_number  refresh  retry  expire   minimum_ttl  
--------------------  -----------------------------  -------------  -------  -----  -------  -----------  
ns-47.awsdns-05.com.  awsdns-hostmaster.amazon.com.  1              7200     900    1209600  86400        

Printing Whois Information



Historical Record Number  1                                                                                                                                                                                                                             
--------------------------------------  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Recorded                                2016-11-03                                                                                                                                                                                                                                  
Whois Server                            whois.corporatedomains.com                                                                                                                                                                                                                  
Referral Url                            www.cscprotectsbrands.com                                                                                                                                                                                                                   
Domain  Name                            cnn.com                                                                                                                                                                                                                                     
Domain  Id                              3269879_DOMAIN_COM-VRSN                                                                                                                                                                                                                     
Domain  Status                          ['serverTransferProhibited http://www.icann.org/epp#serverTransferProhibited', 'serverDeleteProhibited http://www.icann.org/epp#serverDeleteProhibited', 'clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited']      
Date  Updated Date                      2016-11-02T10:00:07Z                                                                                                                                                                                                                        
Date  Creation Date                     1993-09-22T04:00:00Z                                                                                                                                                                                                                        
Date  Registry Expiry Date              2018-09-21T04:00:00Z                                                                                                                                                                                                                        
Registrar  Sponsoring                   CSC CORPORATE DOMAINS, INC.                                                                                                                                                                                                                 
Registrar  Sponsoring  Iana Id          299                                                                                                                                                                                                                                         
Registrar  Abuse Contact Email          domainabuse@cscglobal.com                                                                                                                                                                                                                   
Registrar  Abuse Contact Phone          +1.8887802723                                                                                                                                                                                                                               
Registrant  Name                        Domain Name Manager                                                                                                                                                                                                                         
Registrant  Organization                Turner Broadcasting System, Inc.                                                                                                                                                                                                            
Registrant  Street                      One CNN Center                                                                                                                                                                                                                              
Registrant  City                        Atlanta                                                                                                                                                                                                                                     
Registrant  State/Province              GA                                                                                                                                                                                                                                          
Registrant  Postal Code                 30303                                                                                                                                                                                                                                       
Registrant  Country                     US                                                                                                                                                                                                                                          
Registrant  Phone                       +1.4048275000                                                                                                                                                                                                                               
Registrant  Fax                         +1.4048271995                                                                                                                                                                                                                               
Registrant  Email                       tmgroup@turner.com                                                                                                                                                                                                                          
Admin  Name                             Domain Name Manager                                                                                                                                                                                                                         
Admin  Organization                     Turner Broadcasting System, Inc.                                                                                                                                                                                                            
Admin  Street                           One CNN Center                                                                                                                                                                                                                              
Admin  City                             Atlanta                                                                                                                                                                                                                                     
Admin  State/Province                   GA                                                                                                                                                                                                                                          
Admin  Postal Code                      30303                                                                                                                                                                                                                                       
Admin  Country                          US                                                                                                                                                                                                                                          
Admin  Phone                            +1.4048275000                                                                                                                                                                                                                               
Admin  Fax                              +1.4048271995                                                                                                                                                                                                                               
Admin  Email                            tmgroup@turner.com                                                                                                                                                                                                                          
Tech  Name                              TBS Server Operations                                                                                                                                                                                                                       
Tech  Organization                      Turner Broadcasting System, Inc.                                                                                                                                                                                                            
Tech  Street                            One CNN Center                                                                                                                                                                                                                              
Tech  City                              Atlanta                                                                                                                                                                                                                                     
Tech  State/Province                    GA                                                                                                                                                                                                                                          
Tech  Postal Code                       30303                                                                                                                                                                                                                                       
Tech  Country                           US                                                                                                                                                                                                                                          
Tech  Phone                             +1.4048275000                                                                                                                                                                                                                               
Tech  Fax                               +1.4048271593                                                                                                                                                                                                                               
Tech  Email                             hostmaster@turner.com                                                                                                                                                                                                                       
Name Server  Name                       ['pdns5.ultradns.info', 'ns-1086.awsdns-07.org', 'pdns3.ultradns.org', 'pdns2.ultradns.net', 'pdns6.ultradns.co.uk', 'ns-47.awsdns-05.com', 'ns-1630.awsdns-11.co.uk', 'ns-576.awsdns-08.net', 'pdns1.ultradns.net', 'pdns4.ultradns.org']  


Historical Record Number  2                                                                                                                                                                                                                         
--------------------------------------  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Recorded                                2016-09-16                                                                                                                                                                                                                              
Whois Server                            whois.corporatedomains.com                                                                                                                                                                                                              
Referral Url                            www.cscprotectsbrands.com                                                                                                                                                                                                               
Domain  Name                            cnn.com                                                                                                                                                                                                                                 
Domain  Id                              3269879_DOMAIN_COM-VRSN                                                                                                                                                                                                                 
Domain  Status                          ['serverTransferProhibited http://www.icann.org/epp#serverTransferProhibited', 'serverDeleteProhibited http://www.icann.org/epp#serverDeleteProhibited', 'clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited']  
Date  Updated Date                      2016-09-15T12:02:35Z                                                                                                                                                                                                                    
Date  Creation Date                     1993-09-22T04:00:00Z                                                                                                                                                                                                                    
Date  Registry Expiry Date              2018-09-21T04:00:00Z                                                                                                                                                                                                                    
Registrar  Sponsoring                   CSC CORPORATE DOMAINS, INC.                                                                                                                                                                                                             
Registrar  Sponsoring  Iana Id          299                                                                                                                                                                                                                                     
Registrar  Abuse Contact Email          domainabuse@cscglobal.com                                                                                                                                                                                                               
Registrar  Abuse Contact Phone          +1.8887802723                                                                                                                                                                                                                           
Registrant  Name                        Domain Name Manager                                                                                                                                                                                                                     
Registrant  Organization                Turner Broadcasting System, Inc.                                                                                                                                                                                                        
Registrant  Street                      One CNN Center                                                                                                                                                                                                                          
Registrant  City                        Atlanta                                                                                                                                                                                                                                 
Registrant  State/Province              GA                                                                                                                                                                                                                                      
Registrant  Postal Code                 30303                                                                                                                                                                                                                                   
Registrant  Country                     US                                                                                                                                                                                                                                      
Registrant  Phone                       +1.4048275000                                                                                                                                                                                                                           
Registrant  Fax                         +1.4048271995                                                                                                                                                                                                                           
Registrant  Email                       tmgroup@turner.com                                                                                                                                                                                                                      
Admin  Name                             Domain Name Manager                                                                                                                                                                                                                     
Admin  Organization                     Turner Broadcasting System, Inc.                                                                                                                                                                                                        
Admin  Street                           One CNN Center                                                                                                                                                                                                                          
Admin  City                             Atlanta                                                                                                                                                                                                                                 
Admin  State/Province                   GA                                                                                                                                                                                                                                      
Admin  Postal Code                      30303                                                                                                                                                                                                                                   
Admin  Country                          US                                                                                                                                                                                                                                      
Admin  Phone                            +1.4048275000                                                                                                                                                                                                                           
Admin  Fax                              +1.4048271995                                                                                                                                                                                                                           
Admin  Email                            tmgroup@turner.com                                                                                                                                                                                                                      
Tech  Name                              TBS Server Operations                                                                                                                                                                                                                   
Tech  Organization                      Turner Broadcasting System, Inc.                                                                                                                                                                                                        
Tech  Street                            One CNN Center                                                                                                                                                                                                                          
Tech  City                              Atlanta                                                                                                                                                                                                                                 
Tech  State/Province                    GA                                                                                                                                                                                                                                      
Tech  Postal Code                       30303                                                                                                                                                                                                                                   
Tech  Country                           US                                                                                                                                                                                                                                      
Tech  Phone                             +1.4048275000                                                                                                                                                                                                                           
Tech  Fax                               +1.4048271593                                                                                                                                                                                                                           
Tech  Email                             hostmaster@turner.com                                                                                                                                                                                                                   
Name Server  Name                       ['ns-47.awsdns-05.com', 'ns-1086.awsdns-07.org', 'ns-576.awsdns-08.net', 'ns-1630.awsdns-11.co.uk']                                                                                                                                     


Historical Record Number  3                                                                                               
--------------------------------------  ------------------------------------------------------------------------------------------------------------  
Recorded                                2014-06-23                                                                                                    
Domain  Name                            cnn.com                                                                                                       
Domain  Registry  Id                    3269879_DOMAIN_COM-VRSN                                                                                       
Domain  Status                          ['serverTransferProhibited', 'serverDeleteProhibited', 'clientTransferProhibited', 'serverUpdateProhibited']  
Registrar  Whois Server                 whois.corporatedomains.com                                                                                    
Registrar  Url                          www.cscprotectsbrands.com                                                                                     
Registrar  Name                         CSC CORPORATE DOMAINS, INC.                                                                                   
Registrar  Iana Id                      299                                                                                                           
Registrar  Abuse Contact Email          admin@internationaladmin.com                                                                                  
Registrar  Abuse Contact Phone          +1.8887802723                                                                                                 
Date  Updated Date                      2013-11-27 04:31:40 -0500                                                                                     
Date  Creation Date                     1993-09-22 00:00:00 -0400                                                                                     
Registrant  Name                        Domain Name Manager                                                                                           
Registrant  Organization                Turner Broadcasting System, Inc.                                                                              
Registrant  Street                      One CNN Center                                                                                                
Registrant  City                        Atlanta                                                                                                       
Registrant  State/Province              GA                                                                                                            
Registrant  Postal Code                 30303                                                                                                         
Registrant  Country                     US                                                                                                            
Registrant  Phone                       +1.4048275000                                                                                                 
Registrant  Fax                         +1.4048271995                                                                                                 
Registrant  Email                       tmgroup@turner.com                                                                                            
Admin  Name                             Domain Name Manager                                                                                           
Admin  Organization                     Turner Broadcasting System, Inc.                                                                              
Admin  Street                           One CNN Center                                                                                                
Admin  City                             Atlanta                                                                                                       
Admin  State/Province                   GA                                                                                                            
Admin  Postal Code                      30303                                                                                                         
Admin  Country                          US                                                                                                            
Admin  Phone                            +1.4048275000                                                                                                 
Admin  Fax                              +1.4048271995                                                                                                 
Admin  Email                            tmgroup@turner.com                                                                                            
Tech  Name                              TBS Server Operations                                                                                         
Tech  Organization                      Turner Broadcasting System, Inc.                                                                              
Tech  Street                            One CNN Center                                                                                                
Tech  City                              Atlanta                                                                                                       
Tech  State/Province                    GA                                                                                                            
Tech  Postal Code                       30303                                                                                                         
Tech  Country                           US                                                                                                            
Tech  Phone                             +1.4048275000                                                                                                 
Tech  Fax                               +1.4048271593                                                                                                 
Tech  Email                             hostmaster@turner.com                                                                                         
Name Server  Name                       ['ns1.timewarner.net', 'ns1.p42.dynect.net', 'ns2.p42.dynect.net', 'ns3.timewarner.net']                      


Date        Status          Name Server    
----------  --------------  -------------  
2017-02-15  Transferred to  awsdns-05.com  
2016-11-02  Transferred to  ultradns.org   
2016-09-15  Transferred to  awsdns-05.com  


Type  Hostname  Address                         Preference  TTL  Class  
----  --------  ------------------------------  ----------  ---  -----  
MX    cnn.com   mxa-00241e02.gslb.pphosted.com  10          300  IN     
MX    cnn.com   mxb-00241e02.gslb.pphosted.com  10          300  IN     


Type  Hostname  Address         TTL  Class  
----  --------  --------------  ---  -----  
A     cnn.com   151.101.1.67    60   IN     
A     cnn.com   151.101.65.67   60   IN     
A     cnn.com   151.101.129.67  60   IN     
A     cnn.com   151.101.193.67  60   IN     
Record Type                     Record Data                                                                                                                                                                                                                             
------------------------------  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Domain                          cnn.com                                                                                                                                                                                                                                 
Words In                        cnn                                                                                                                                                                                                                                     
Ip Address                      151.101.65.67                                                                                                                                                                                                                           
Ip Geo Location                 United States, California, San Francisco                                                                                                                                                                                                
Title                           CNN - Breaking News, Latest News and Videos                                                                                                                                                                                             
Date Creation                   1993-09-22                                                                                                                                                                                                                              
Web Age                         28 years and 2 months                                                                                                                                                                                                                   
Name                            Domain Name Manager                                                                                                                                                                                                                     
Organization                    Turner Broadcasting System Inc                                                                                                                                                                                                          
Email                           tmgroup@turner.com                                                                                                                                                                                                                      
Address                         One CNN Center                                                                                                                                                                                                                          
City                            Atlanta                                                                                                                                                                                                                                 
State                           GA                                                                                                                                                                                                                                      
Country                         United States                                                                                                                                                                                                                           
Phone                           +1.4048275000                                                                                                                                                                                                                           
Fax                             +1.4048271995                                                                                                                                                                                                                           
Private                         no                                                                                                                                                                                                                                      
Record Date                      2017-02-16                                                                                                                                                                                                                             
Domain Name                      cnn.com                                                                                                                                                                                                                                
Registry Domain Id               3269879_DOMAIN_COM-VRSN                                                                                                                                                                                                                
Registrar  Whois Server         whois.corporatedomains.com                                                                                                                                                                                                              
Registrar  Url                  www.cscprotectsbrands.com                                                                                                                                                                                                               
Registrar  Name                 CSC CORPORATE DOMAINS, INC.                                                                                                                                                                                                             
Registrar  Iana Id              299                                                                                                                                                                                                                                     
Registrar  Abuse Contact Email  domainabuse@cscglobal.com                                                                                                                                                                                                               
Registrar  Abuse Contact Phone  +1.8887802723                                                                                                                                                                                                                           
Date  Updated Date              2017-02-15T16:01:26Z                                                                                                                                                                                                                    
Date  Creation Date             1993-09-22T04:00:00Z                                                                                                                                                                                                                    
Domain  Status                  ['clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited', 'serverDeleteProhibited http://www.icann.org/epp#serverDeleteProhibited', 'serverTransferProhibited http://www.icann.org/epp#serverTransferProhibited']  
Registrant  Name                Domain Name Manager                                                                                                                                                                                                                     
Registrant  Organization        Turner Broadcasting System, Inc.                                                                                                                                                                                                        
Registrant  Street              One CNN Center                                                                                                                                                                                                                          
Registrant  City                Atlanta                                                                                                                                                                                                                                 
Registrant  State/Province      GA                                                                                                                                                                                                                                      
Registrant  Postal Code         30303                                                                                                                                                                                                                                   
Registrant  Country             US                                                                                                                                                                                                                                      
Registrant  Phone               +1.4048275000                                                                                                                                                                                                                           
Registrant  Fax                 +1.4048271995                                                                                                                                                                                                                           
Registrant  Email               tmgroup@turner.com                                                                                                                                                                                                                      
Admin  Name                     Domain Name Manager                                                                                                                                                                                                                     
Admin  Organization             Turner Broadcasting System, Inc.                                                                                                                                                                                                        
Admin  Street                   One CNN Center                                                                                                                                                                                                                          
Admin  City                     Atlanta                                                                                                                                                                                                                                 
Admin  State/Province           GA                                                                                                                                                                                                                                      
Admin  Postal Code              30303                                                                                                                                                                                                                                   
Admin  Country                  US                                                                                                                                                                                                                                      
Admin  Phone                    +1.4048275000                                                                                                                                                                                                                           
Admin  Fax                      +1.4048271995                                                                                                                                                                                                                           
Admin  Email                    tmgroup@turner.com                                                                                                                                                                                                                      
Tech  Name                      TBS Server Operations                                                                                                                                                                                                                   
Tech  Organization              Turner Broadcasting System, Inc.                                                                                                                                                                                                        
Tech  Street                    One CNN Center                                                                                                                                                                                                                          
Tech  City                      Atlanta                                                                                                                                                                                                                                 
Tech  State/Province            GA                                                                                                                                                                                                                                      
Tech  Postal Code               30303                                                                                                                                                                                                                                   
Tech  Country                   US                                                                                                                                                                                                                                      
Tech  Phone                     +1.4048275000                                                                                                                                                                                                                           
Tech  Fax                       +1.4048271593                                                                                                                                                                                                                           
Tech  Email                     hostmaster@turner.com                                                                                                                                                                                                                   
Name Server  Name               ['ns-1630.awsdns-11.co.uk', 'ns-576.awsdns-08.net', 'ns-47.awsdns-05.com', 'ns-1086.awsdns-07.org']                                                                                                                                     
````

## Documentation

You can find documents on following links

- https://iabdullahmughal.github.io/domain-trails/