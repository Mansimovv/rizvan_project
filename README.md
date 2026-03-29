# Student Club Registration System

## Layihənin Məqsədi

Bu sistem universitet tələbələrinin müxtəlif klublara qeydiyyatını və qoşulmasını asanlaşdırır. İstifadəçilər qeydiyyatdan keçə, login ola, klublara qoşula və öz qoşulduqları klubları görə bilərlər. Bütün məlumatlar təhlükəsiz şəkildə saxlanılır və idarə olunur.

## Əsas Texnologiyalar

- Python 3
- Django 6
- Django Templates (HTML, CSS, Bootstrap)
- SQLite (default Django database)
- Django ORM

## Arxitektura və Struktur

**Backend:**
- Django əsaslıdır, bütün biznes məntiqi və məlumat bazası əməliyyatları server tərəfindədir.
- `accounts` app: istifadəçi qeydiyyatı, login/logout, profil.
- `clubs` app: klubların siyahısı, kluba qoşulma, üzvlük.

**Frontend:**
- Django templateləri və Bootstrap ilə hazırlanıb.
- Bütün səhifələr server tərəfindən render olunur (SPA və ya REST API yoxdur, klassik monolit arxitektura).

**Front-Back Əlaqəsi:**
- İstifadəçi brauzerdə formu doldurur → POST request Django serverə gedir → serverdə yoxlanılır və nəticə ilə yeni səhifə render olunur.
- AJAX və ya API endpoint-lər yoxdur, bütün əməliyyatlar klassik HTTP request/response ilədir.

## Əsas URL-lər və Səhifələr

| URL | Səhifə/Funksiya | Açıklama |
|---|---|---|
| `/` | Home | Ana səhifə, qısa info |
| `/register/` | Qeydiyyat | Yeni istifadəçi qeydiyyatı |
| `/login/` | Daxil ol | İstifadəçi login |
| `/logout/` | Çıxış | Sessiyanı bitirir |
| `/clubs/` | Klublar | Bütün klubların siyahısı |
| `/clubs/join/<id>/` | Kluba qoşul | Seçilmiş kluba qoşulma |
| `/clubs/my-clubs/` | Mənim klublarım | İstifadəçinin qoşulduğu klublar |
| `/admin/` | Admin panel | Klub və üzvlükləri idarə etmək üçün |

## Model Əlaqələri və Məlumat Axını

- **User (Django User modeli):** Sistemdə qeydiyyatdan keçən hər kəs.
- **Profile:** User ilə OneToOne bağlıdır, əlavə olaraq full_name və email saxlayır.
- **Club:** Klubun adı, təsviri və yaradılma tarixi.
- **Membership:** User və Club arasında ManyToMany əlaqəni təmsil edir (hər user bir kluba yalnız bir dəfə qoşula bilər).

## İstifadəçi Axını

1. **Qeydiyyat:**
	- İstifadəçi `/register/` səhifəsində formu doldurur.
	- Username və email unikal olmalıdır, şifrə təhlükəsiz saxlanılır.
	- Qeydiyyat uğurlu olduqda login səhifəsinə yönləndirilir və uğurlu mesaj göstərilir.

2. **Login/Logout:**
	- İstifadəçi `/login/` səhifəsində daxil olur.
	- Uğurlu login olduqda ana səhifəyə yönləndirilir.
	- `/logout/` ilə çıxış edə bilər.

3. **Klublar və Qoşulma:**
	- `/clubs/` səhifəsində bütün klublar list şəklində göstərilir.
	- İstifadəçi istədiyi kluba qoşula bilər (yalnız bir dəfə).
	- Qoşulduğu klubları `/clubs/my-clubs/` səhifəsində görə bilər.

4. **Admin Panel:**
	- `/admin/` ünvanında admin panel var.
	- Buradan klubları əlavə/sil/redaktə etmək və istifadəçilərin üzvlüyünü izləmək mümkündür.

## Quraşdırma və İşə Salma

1. Virtual environment yaradın və aktiv edin:
	```bash
	python -m venv venv
	venv\Scripts\activate
	```
2. Tələbləri quraşdırın:
	```bash
	pip install -r requirements.txt
	```
3. Migrasiyaları tətbiq edin:
	```bash
	python manage.py makemigrations accounts clubs
	python manage.py migrate
	```
4. Superuser yaradın:
	```bash
	python manage.py createsuperuser
	```
5. Test üçün bəzi klublar əlavə edin:
	```bash
	python manage.py shell
	from clubs.models import Club
	Club.objects.create(name="Programming Club", description="Kodlaşdırma və proqramlaşdırma həvəskarları üçün klub.")
	Club.objects.create(name="Chess Club", description="Şahmat həvəskarları üçün klub.")
	Club.objects.create(name="English Speaking Club", description="İngilis dili danışıq klubudur.")
	Club.objects.create(name="Cyber Security Club", description="Kiber təhlükəsizlik mövzusunda klub.")
	exit()
	```
6. Serveri işə salın:
	```bash
	python manage.py runserver
	```

## Qovluq Strukturu

```
student_club_system/
├── manage.py
├── requirements.txt
├── student_club_system/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── accounts/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── clubs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── accounts/
│   │   ├── register.html
│   │   └── login.html
│   └── clubs/
│       ├── club_list.html
│       └── my_clubs.html
└── static/
	 └── css/
		  └── style.css
```

## Əlavə Qeydlər

- Layihə tamamilə Django server-side rendering üzərində qurulub.
- API və ya SPA yoxdur, bütün əməliyyatlar klassik form submit və redirect-lərlə aparılır.
- Bootstrap və öz CSS ilə səliqəli, mobil uyğun dizayn.
- İstifadəçi və admin üçün fərqli imkanlar mövcuddur.

**Suallarınız və ya əlavə ehtiyacınız olarsa, müraciət edə bilərsiniz!**