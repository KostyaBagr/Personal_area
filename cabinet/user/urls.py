from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
app_name='user'
urlpatterns =[
    path('', index, name='index'),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration')


]

