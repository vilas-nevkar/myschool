from django.urls import path
# from .views import dashboard
from . import views


app_name = 'account'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.staff_register, name='register'),
]