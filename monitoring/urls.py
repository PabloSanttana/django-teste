from django.urls import path

from . import views

app_name = 'monitoring'

urlpatterns = [
    path("monitoring/", views.home, name="home")
]
