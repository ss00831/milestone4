from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tourprograms, name='tourprograms'),
    path('<tourprogram_id>', views.tourprogram_detail, name='tourprogram_detail'),
]
