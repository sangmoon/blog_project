Provisioning a new site
=======================

##Required packages:

* nginx
*Python 3
*Git
*pip
*virtualenv

eg, on Ubuntu:
```shell
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv
```

## Nginx Virtual Host config

* see nginx.template.conf
*replace SITENAME with, eg, www.sangmoonpark.com

##Upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, www.sangmoonpark.com 

##Folder structure:
Assume we have auser account at /home/username


/home/username    
└── sites    
    └── SITENAME    
         ├── database    
         ├── source    
         ├── static    
         └── virtualenv    

