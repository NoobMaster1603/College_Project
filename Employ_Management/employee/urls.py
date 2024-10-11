from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.form_view, name='home'),
    path('success/', views.success_view, name='success'),
]