
from django.urls import path
from users import views

urlpatterns = [
   
    path('',views.reg,name='reg'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('profile',views.profile_view,name='profile'),
    path('list', views.profile_list, name='list'),
    path('update<int:id>',views.update_profile,name='update'),
    path('reset_password/', views.reset_password, name='reset_password'),

]