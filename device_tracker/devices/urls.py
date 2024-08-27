from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.device_CreateView.as_view(), name='add_device'),
    path('list/', views.device_ListView.as_view(), name='list_devices'),
    path('search/', views.search_device, name='search_device'),
]