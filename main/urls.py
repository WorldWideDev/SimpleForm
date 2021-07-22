from django.urls import path
from main import views
urlpatterns = [
    path('', views.index),
    path('do_it', views.do_it),
]