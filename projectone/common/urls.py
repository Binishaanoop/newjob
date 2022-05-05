from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('class2/', views.class2, name='class2'),
    path('placed_candidate/', views.placed_candidate, name='placed_candidate'),
    path('empreg/', views.empreg, name='empreg'),
    path('emplog/', views.emplog, name='emplog'),
    path('register/', views.register, name='register')
]
