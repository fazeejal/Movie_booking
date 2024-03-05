from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.details, name='details'),  # Corrected 'details' from 'detalis'
     path('delete/<int:id>/',views.delete,name='delete'),
     path('update/<int:movie_id>/', views.update, name='update'),
]
