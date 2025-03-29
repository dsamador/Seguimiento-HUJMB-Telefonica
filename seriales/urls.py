from django.urls import path
from .views import Vista

urlpatterns = [
    path('', Vista, name='dashboard'),
]
