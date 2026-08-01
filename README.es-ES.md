

# docker-archer

Plataforma automatizada para operaciones SQL basada en Inception y Archer, con soporte para tickets, revisión, autenticación, correo electrónico y OSC, entre otras funciones.


##### Configuración de la base de datos
Crear una base de datos con codificación utf-8

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
##### Crear tablas

```
1: python3 manage.py makemigrations或python3 manage.py makemigrations sql
2: python3 manage.py migrate
3: cd /archer && python3 manage.py createsuperuser // 创建初始用户
```

##### Iniciar el servicio

```
make
```
Acceda en el navegador a http://127.0.0.1:8080

------
archer: https://github.com/jly8866/archer
inception: https://github.com/mysql-inception/inception
