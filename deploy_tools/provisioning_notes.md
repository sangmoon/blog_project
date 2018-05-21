Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* git
* pip

eg, on Ubuntu:
```shell
    sudo apt-get install nginx git python3 python3-pip
```

## Nginx Virtual Host config
* this files locate at ``/etc/nginx/sites-available``
* see nginx.template.conf
* replace SITENAME with, eg, www.sangmoonpark.com
```shell
//for restart
sudo service nginx reload
sudo systemctl restart nginx
```



## Systemd job
* this file locate at ``/etc/systemd/system``
* see gunicorn-systemd.tetmplate.service
* replace SITENAME with, eg, www.sangmoonpark.com 
```shell
//for restart
sudo systemctl restart gunicorn-SITENAME
```


## Folder structure:
Assume we have a user account at /home/username


/home/username    
└── sites    
    └── SITENAME    
         ├── database    
         ├── source    
         ├── static    
         └── virtualenv    

