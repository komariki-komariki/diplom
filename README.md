Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
* Осуществить миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создать суперпользователя
```bash
python manage.py createsuperuser
```

* Запустить приложение
```bash
python manage.py runserver
```
* Приложение доступно локально по адресу: http://127.0.0.1:8000/
