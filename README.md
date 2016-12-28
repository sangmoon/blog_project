## Blog-project
**개인 블로그 제작**  

1. working on server  
2. can wirte a note  
3. can sign up, log in, log out  
4. 사람들마다 자신의 글을 모아볼 수 있는 시스템.  

-------------
1. make a project  
```python
django-admin makeproject myblog
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
