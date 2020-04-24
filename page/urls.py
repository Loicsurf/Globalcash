from django.urls import path
from page import views

from .views import emailView, successView

urlpatterns = [
	path('', views.Globalcash, name='Globalcash'),
	path('login/', views.login, name='login'),
	path('vip/', views.vip, name='vip'),
	path('services/', views.services, name='services'),
	path('about/', views.about, name='about'),
	path('logout/', views.logout, name='logout'),
	path('contact/', views.contact, name='contact'),
	path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]