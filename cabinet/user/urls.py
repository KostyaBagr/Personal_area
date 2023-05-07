from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
app_name='user'
urlpatterns =[
    path('', index, name='index'),

    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html',email_template_name='user/password_reset_email.html',success_url=reverse_lazy('user:password_reset_done')), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(template_name='user/password_sent_form.html',success_url=reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_done.html'), name='password_reset_complete'),
]

