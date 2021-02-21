from django.urls import path
from . import views

app_name = "surveys"

urlpatterns = [
    path('', views.survey, name='survey'),
    path('presurveys', views.presurvey, name='presurvey'),
    path('aftersurveys', views.aftersurvey, name='aftersurvey'),
]
