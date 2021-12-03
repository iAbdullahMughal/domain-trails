Getting Started
===============

Domain tails is python tool based on free available sources
for domain information collection.

Installation
************

Preparing installation
----------------------

Install python3 on system. Currently project has zero external
dependency verify python version::

    python -V
    Python 3.6.8

.. note:: Project is currently supported with python3+ versions.



Cloning Project
---------------

Clone repo on system / server::

    git clone https://github.com/iAbdullahMughal/domain-trails.git

Your file system should now look similar to this::

    domain-trails
    ├── docs
    ├── LICENSE
    ├── README.md
    ├── portal.py
    ├── setup.py
    └── core
        ├── parser
        ├── recon
        ├── __init__.py
        └── resources.py

We have a top-level ``portal.py`` directory in the main project directory.
.. warning:: Project directory structure may change.

Executing Project
-----------------

Project without parameters::


    python .\portal.py
    -------------------------------------------------------------------------------
          ____                            _           ______              _  __
         / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
        / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
       / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  )
      /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/
      -------------------------------------------------------------------------------
        Domain Trails - domains footprints, reconnaissance & information gathering
      -------------------------------------------------------------------------------
    usage: portal.py [-h] -d DOMAIN
    portal.py: error: the following arguments are required: -d




Run project with parameter::

    python .\portal.py -d www.google.com
    -------------------------------------------------------------------------------
          ____                            _           ______              _  __
         / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
        / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
       / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  )
      /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/
      -------------------------------------------------------------------------------
        Domain Trails - domains footprints, reconnaissance & information gathering
      -------------------------------------------------------------------------------
      Printing Results for domain www.google.com

Supported Modules
*****************
.. note:: Actively adding more modules for more coverage.

Following modules are supported in domain trails

☑️Domain Availability Check
-----------------------------
Output::

    Domain Availability Result for www.google.com : Domain is Registered

📜️Domain Hosting History
--------------------------
Output::

    DNS History Records

    Old Web Host  New Web Host  Month / Year   Zone Date  Transaction
    ------------  ------------  -------------  ---------  -----------
    google.com    n/a           december 2000             epoch

📇️️Domain DNS Information
--------------------------
Output::

    IP v6 Records

    name         type  class  ttl  endpoint
    -----------  ----  -----  ---  ------------------------
    google.com.  AAAA  IN     300  2607:f8b0:4006:817::200e

    Mail eXchanger (MX) Records

    name         type  class  ttl  endpoint
    -----------  ----  -----  ---  ---------------------------
    google.com.  MX    IN     600  30 alt2.aspmx.l.google.com.
    google.com.  MX    IN     600  50 alt4.aspmx.l.google.com.
    google.com.  MX    IN     600  10 aspmx.l.google.com.
    google.com.  MX    IN     600  20 alt1.aspmx.l.google.com.
    google.com.  MX    IN     600  40 alt3.aspmx.l.google.com.

    Parent Name Server records

    name         type  class  ttl  endpoint
    -----------  ----  -----  ---  --------------
    google.com.  A     IN     300  142.250.81.238

    Local Name Server Records

    name         type  class  ttl     endpoint
    -----------  ----  -----  ------  ---------------
    google.com.  NS    IN     271654  ns4.google.com.
    google.com.  NS    IN     271654  ns3.google.com.
    google.com.  NS    IN     271654  ns1.google.com.
    google.com.  NS    IN     271654  ns2.google.com.

    Start of Authority (SOA)

    primary_nameserver  host_master_email      serial_number  refresh  retry  expire  minimum_ttl
    ------------------  ---------------------  -------------  -------  -----  ------  -----------
    ns1.google.com.     dns-admin.google.com.  413628036      900      900    1800    60

    Text Records

    name         type  class  ttl   endpoint
    -----------  ----  -----  ----  --------------------------------------------------------------------
    google.com.  TXT   IN     3600  facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95
    google.com.  TXT   IN     3600  google-site-verification=wD8N7i1JTNTkezJ49swvWW48f8_9xveREV4oB-0Hf5o
    google.com.  TXT   IN     3600  docusign=1b0a6754-49b1-4db5-8540-d2c12664b289
    google.com.  TXT   IN     3600  globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=
    google.com.  TXT   IN     3600  google-site-verification=TV9-DBe4R80X4v0M4U_bd_J9cpOJM0nikft0jAgjmsQ
    google.com.  TXT   IN     3600  "v=spf1 include:_spf.google.com ~all"
    google.com.  TXT   IN     3600  docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e
    google.com.  TXT   IN     3600  MS=E4A68B9AB2BB9670BCE15412F62916164C0B20BB
    google.com.  TXT   IN     3600  apple-domain-verification=30afIBcvSuDV2PLX

.. warning::
    Domain name records may change there
