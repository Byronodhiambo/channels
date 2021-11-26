from django.urls import path
from . import views

appname = 'directmessage'

urlpatterns = [
    path('', views.index, name='index'),
]
