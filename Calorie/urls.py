from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('user/',views.userPage,name='userPage'), 
    path('fooditem/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    path('addFooditem/',views.addFooditem,name='addFooditem'),

    path('user/<int:pk>/update/', views.ItemUpdate.as_view(), name='fooditemupdate'),
    path('user/<int:pk>/delete/', views.ItemDelete.as_view(), name='fooditemdelete'),
   
]