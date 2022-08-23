# docker-archer

基于inception和archer的自动化SQL操作平台，支持工单、审核、认证、邮件、OSC等功能


##### 数据库配置
创建符合utf-8编码的数据库

```shell
make mysql
```

```shell
# archer/apps/srv/archer/archer/settings/dev.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'archer',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'archer_mysql',
        'PORT': '3306'
    }
}
```
##### 创建数据表

```
1: python3 manage.py makemigrations或python3 manage.py makemigrations sql
2: python3 manage.py migrate
3: cd /archer && python3 manage.py createsuperuser // 创建初始用户
```

##### 启动服务

```
make
```
浏览器访问 http://127.0.0.1:8080

------
archer: https://github.com/jly8866/archer
inception: https://github.com/mysql-inception/inception
