from django.urls import path
from . import views
from .views import AppointmentView


app_name = 'mails'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('mails', AppointmentView.as_view(), name='mails'),
    path('create/', views.create, name='create'),

]