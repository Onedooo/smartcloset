from django.urls import path

from . import views

urlpatterns = [
    path('save/', views.save_data),
    path('check/<int:accountid>/', views.check_data),
    path('edit/<int:pk>/', views.edit_data),
    path('remove/<int:pk>/', views.remove_data),
]
