
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('addnew/', views.addnewPage),
    path('add_todo/',views.add_todo),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('register/', views.registerPage),
    path('delete-todo/<int:id>/',views.delete_todo),

]
