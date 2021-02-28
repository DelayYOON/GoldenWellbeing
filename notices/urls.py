from django.urls import path
from . import views

app_name = "notices"

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:post_id>/', views.detail, name='detail'),
    path('info', views.info, name='info'),
]
