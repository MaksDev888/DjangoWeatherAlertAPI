# DjangoWeatherAlert - Сервис для получение актуальных данных о погоде и уведомлении о ней посредством email.

DjangoWeatherAlert - это сервис помогающий получить актульные даныне о погоде в любой точке мира, а также имееться возможность получать уведомелния каждые 1/3/6/12 часов о текущей погоде на email.

>Технологии, используемые на проекте:


>>1. Python ![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
>>2. Django ![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
>>3. DjangoRestFramework ![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
>>4. PostgresSQL ![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)
>>5. pgAdmin ![pgAdmin](https://img.shields.io/badge/PG-pgAdmin-blue?style=flat-square&logo=pgAdmin)
>>6. Celery ![Celery](https://img.shields.io/badge/-Celery-%2300C7B7?style=flat-square&logo=Celery)
>>7. Flower ![Flower](https://img.shields.io/badge/F-Flower-green?style=flat-square&logo=Celery)
>>8. Redis ![Redis](https://img.shields.io/badge/-Redis-FCA121?style=flat-square&logo=Redis)

# Как запустить проект:

В папку Проекта расположить .env файл со следующими параметрами:

1. DB_NAME=**Имя БД**
2. DB_USER=**Имя пользователя БД**
3. DB_PASSWORD=**Пароль БД**
4. DB_HOST=**Хост или адресс БД**
5. DB_PORT=**Порт БД**
6. DJANGO_SECRET_KEY =**Секретный ключ вашего проекта**
7. WEATHER_API_KEY=**Ваш API ключ с openweathermap**
8. EMAIL_HOST_USER=**Имя пользователя, которое будет использоваться для SMTP-сервера**
9. EMAIL_HOST_PASSWORD=**Пароль, который будет использоваться для SMTP-сервера**

Скачать docker: 
1. Для [windows](https://docs.docker.com/desktop/windows/install/)
2. Для [macOS](https://docs.docker.com/desktop/mac/install/)
3. Для дистрибутивов [Linux](https://docs.docker.com/desktop/linux/#uninstall)

После установки проверьте конфигурацию переменных окружений 
командой:
```
docker-compose config
```
Если всё успешно, все переменные на местах, запустить командой:
```
docker-compose -f docker-compose.dev.yml up --build -d
```

Что бы создать суперпользователя, 
необходимо войти в контейнер командой:
```
docker exec -it dwa_app bash
```
Применить миграции:
```
python manage.py migrate
```
Собрать статику:
```
python manage.py collectstatic
```
После ввести команду:
```
python manage.py createsuperuser
```
и следовать дальнейшим инструкциям.

Для выхода введите:
```
exit
```
