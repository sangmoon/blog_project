## Blog-project
**개인 블로그 제작**  

1. working on server  
2. can wirte a note  
3. can sign up, log in, log out   

-------------
1. make a project  
```python
django-admin startproject myblog
```

2. make an app
```python
python manage.py startapp app
```
---------

## deploy
deploy 는 배포
nginx는 서버 재시작
gunicorn으로 소켓 재설정
```
$ fab deploy:host=smant@www.sangmoonpark.com
$ fab nginx:host=smant@www.sangmoonpark.com
$ fab gunicorn:host=smant@www.sangmoonpark.com
```
---
## Stack
django2.0
jquery3.1
bootstrap3.3.7
postgresql 9.6 

- https 인증을 위해 gogetssl.com의 comodo free ssl을 이용했다. (3개월마다 갱신 필요)
