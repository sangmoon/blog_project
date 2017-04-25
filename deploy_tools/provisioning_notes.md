Provisioning a new site
=======================

##Required packages:

*nginx
*Python 3
*git
*pip

eg, on Ubuntu:
```shell
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv
```

## Nginx Virtual Host config
* this files locate at ``/etc/nginx/sites-available``, ``/etc/nginx/sites-enable``
* see nginx.template.conf
*replace SITENAME with, eg, www.sangmoonpark.com

##Upstart job
* this file locate at ``/etc/init/``
* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, www.sangmoonpark.com 

##Folder structure:
Assume we have a user account at /home/username


/home/username    
└── sites    
    └── SITENAME    
         ├── database    
         ├── source    
         ├── static    
         └── virtualenv    

