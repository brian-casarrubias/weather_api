
from django.urls import path
from weather import views

urlpatterns = [
    path('today/', views.home, name='home-page'),
   
   
]
