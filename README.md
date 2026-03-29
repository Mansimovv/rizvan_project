# Student Club Registration System

## Quraşdırma və işə salma

1. Virtual environment yaradın və aktiv edin:

```
python -m venv venv
venv\Scripts\activate
```

2. Tələbləri quraşdırın:
```
pip install -r requirements.txt
```

3. Migrasiyaları tətbiq edin:
```
python manage.py makemigrations accounts clubs
python manage.py migrate
```

4. Superuser yaradın:
```
python manage.py createsuperuser
```

5. Test üçün bəzi klublar əlavə edin:
```
python manage.py shell
>>> from clubs.models import Club
>>> Club.objects.create(name="Programming Club", description="Kodlaşdırma və proqramlaşdırma həvəskarları üçün klub.")
>>> Club.objects.create(name="Chess Club", description="Şahmat həvəskarları üçün klub.")
>>> Club.objects.create(name="English Speaking Club", description="İngilis dili danışıq klubudur.")
>>> Club.objects.create(name="Cyber Security Club", description="Kiber təhlükəsizlik mövzusunda klub.")
>>> exit()
```

6. Serveri işə salın:
```
python manage.py runserver
```

## Əsas URL-lər

- `/` - Home
- `/register/` - Qeydiyyat
- `/login/` - Daxil ol
- `/logout/` - Çıxış
- `/clubs/` - Klublar
- `/clubs/join/<id>/` - Kluba qoşul
- `/clubs/my-clubs/` - Mənim klublarım

## Admin panel
- `/admin/` - Klub və üzvlükləri idarə etmək üçün