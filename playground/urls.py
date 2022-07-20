from django.urls import path
from . import views
# OUR URL CONFIGRATION
urlpatterns = [
    path('hello/', views.sayHello)
]
