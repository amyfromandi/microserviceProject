from django.urls import path
from . import views

urlpatterns = [
    path('postlatlong/', views.post_birds)
]