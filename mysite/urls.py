from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('page/', views.single_page, name='single_page'),
]