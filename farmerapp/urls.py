from django.urls import path

from . import views

urlpatterns = [

    path("", views.index),
    path("saleform", views.saleform, name='saleform'),
    path("salereq", views.salereq, name='salereq'),
    path("register", views.register, name='register'),
    path("login_view", views.login_view, name='login_view')

]