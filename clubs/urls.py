from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='clubs'),
    path('join/<int:club_id>/', views.join_club, name='join_club'),
    path('my-clubs/', views.my_clubs, name='my_clubs'),
]
