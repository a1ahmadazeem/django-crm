from django.urls import path
from . import views
# from .views import register

urlpatterns=[
    path('',views.home,name=''),
    path('register', views.register,name='register'),
    path('my-login', views.login,name='my-login'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('user_logout' ,views.user_logout,name='user_logout'),
    path('create_record' ,views.create_record,name='create_record'),
    path('update-record/<int:pk>',views.update_record,name='update-record'),
    path('record/<int:pk>',views.singular_record,name='record'),
    path('delete-record/<int:pk>',views.delete_record,name='delete-record'),

]