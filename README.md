# docker-archer
基于inception和archer的自动化SQL操作平台，支持工单、审核、认证、邮件、OSC等功能

## 使用说明

### 使用方法
如果本地存在数据库：
```
// 必须基于本地已经创建了数据库服务
./run.sh
```
* 浏览器访问 http://127.0.0.1:8080

### 数据库配置
* 如果本地存在数据库，略过
* 创建符合utf-8编码的数据库

```
cd mysql
./run-sql-server.sh
```

```
# archer/dev.py 配置数据库连接
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
* 创建数据表

```
1: python3 manage.py makemigrations或python3 manage.py makemigrations sql
2: python3 manage.py migrate
3: cd /archer && python3 manage.py createsuperuser // 创建初始用户
```
```
./run.sh
```

### inception
* 一个集审核、执行、备份及生成回滚语句于一身的MySQL自动化运维工具
* github地址: https://github.com/mysql-inception/inception
