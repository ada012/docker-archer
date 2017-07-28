from archer.settings.base import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'archer',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# inception组件所在的地址
INCEPTION_HOST = 'inception'
INCEPTION_PORT = '6100'

# 查看回滚SQL时候会用到，这里要告诉archer去哪个mysql里读取inception备份的回滚信息和SQL.
# 注意这里要和inception组件的inception.conf里的inception_remote_XX部分保持一致.
INCEPTION_REMOTE_BACKUP_HOST = 'inception'
INCEPTION_REMOTE_BACKUP_PORT = 5621
INCEPTION_REMOTE_BACKUP_USER = 'inception'
INCEPTION_REMOTE_BACKUP_PASSWORD = 'inception'

# 是否开启邮件提醒功能：发起SQL上线后会发送邮件提醒审核人审核，执行完毕会发送给DBA. on是开，off是关，配置为其他值均会被archer认为不开启邮件功能
MAIL_ON_OFF = 'on'

MAIL_REVIEW_SMTP_SERVER = 'mail.xxx.com'
MAIL_REVIEW_SMTP_PORT = 25
MAIL_REVIEW_FROM_ADDR = 'archer@xxx.com'  # 发件人，也是登录SMTP server需要提供的用户名
MAIL_REVIEW_FROM_PASSWORD = ''  # 发件人邮箱密码，如果为空则不需要login SMTP server
MAIL_REVIEW_DBA_ADDR = ['zhangsan@abc.com', 'lisi01@abc.com']  # DBA地址，执行完毕会发邮件给DBA，以list形式保存