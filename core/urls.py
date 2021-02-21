from django.urls import path
from lectures import views as lectures_views

app_name = "core"

# urlpatterns = [path("", lectures_views.all_lectures, name="home")]
urlpatterns = [path("", lectures_views.HomeView.as_view(), name="home")]