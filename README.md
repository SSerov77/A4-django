# A5-django

## Как запустить проект

* Склонировать проект:
```bash
git clone https://github.com/SSerov77/A4-django.git
```

* Перейти в склоннированную папку проекта:
```bash
cd A4-django
```

* Создать папку с виртуальным окружением:
```bash
python -m venv venv
```

* Активировать виртуальное окружение <i>(советую в cmd, тк по умолчанию в VSCode создается терминал Powershell)</i>
```bash
venv\Scripts\activate
```

* Установить необходимые библиотеки:
```bash
pip install -r requirements.txt
```

Перейти в папку с приложением:
```bash
cd a4
```

Запустить файл запуска:
```bash
python manage.py runserver
```
Пример запуска:
[![image.png](https://i.postimg.cc/rpBzycdj/image.png)](https://postimg.cc/06C9ZT0K)

* Перейти в браузере по ссылке:
```bash
http://127.0.0.1:8000/
```


## Как создать базу данных

* Создать миграции: 
```bash
python manage.py makemigrations
```
Пример:
[![image.png](https://i.postimg.cc/SKT7gnvs/image.png)](https://postimg.cc/8Fv65zDQ)

* Применить миграции:
```bash
python manage.py migrate
```
Пример:
[![image.png](https://i.postimg.cc/NfkXNyyc/image.png)](https://postimg.cc/PPNNJ5z3)


## Как создать Администратора

* Создать суперпользователя:
```bash
python manage.py createsuperuser
```

* Заполнить данные аккаунта, пример:
[![image.png](https://i.postimg.cc/R0VL17Gy/image.png)](https://postimg.cc/4YqcshDQ)

* Чтобы перейти на Панель Администратора нужно перейти по ссылке:
```bash
http://127.0.0.1:8000/admin
```
