from django.urls import path
from . import views

urlpatterns = [
    path('ourhomes',views.ourhomes,name='ourhomes'),
    path('enterhome',views.enterhome,name='enterhome'),
]