from django.urls import path
from . import views
urlpatterns = [
   
   path('', views.signin, name='signin'),
   path('signup/',views.signup, name='signup'),
   path('dashboard/',views.dashboard , name='dashboard'),
   path("edit/<int:todo_id>/", views.edit_todo, name="edit_todo"),
   path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
     path('logout/', views.user_logout, name='logout'),
]