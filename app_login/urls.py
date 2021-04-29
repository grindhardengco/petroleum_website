from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success_login',views.success_login),
    path('edit_account', views.edit_account),
    path('update_account', views.update_account),
    path('logout', views.logout),
]