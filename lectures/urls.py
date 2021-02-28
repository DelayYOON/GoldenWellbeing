from django.urls import path
from . import views

app_name = "lectures"

urlpatterns = [
    path('', views.lecture, name='lecture'),
    path('lecture1', views.lecture1, name='lecture1'),
    path('lecture2', views.lecture2, name='lecture2'),
    path('lecture3', views.lecture3, name='lecture3'),
    path('lecture4', views.lecture4, name='lecture4'),
    path('lecture5', views.lecture5, name='lecture5'),
    path('lecture6', views.lecture6, name='lecture6'),
    path('lecture7', views.lecture7, name='lecture7'),
    path('lecture8', views.lecture8, name='lecture8'),
]
