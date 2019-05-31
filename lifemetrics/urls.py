from django.urls import path
from lifemetrics import views

urlpatterns = [
    path('', views.test, name='home'),
]
