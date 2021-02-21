from django.urls import path
from . import views

app_name = "lectures"

urlpatterns = [
    path('', views.lecture, name='lecture'),
]
