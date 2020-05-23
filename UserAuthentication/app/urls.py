from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app/signup',views.signup,name='signup')
]