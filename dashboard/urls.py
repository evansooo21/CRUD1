from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserRegisterView, dashboard, Reg_comp, edit, logout_view
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('dashboard/',dashboard, name="dashboard"),
    path('Register_done/', Reg_comp, name="regcomp"),
    path('edit/', edit, name="edit"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('logout/', logout_view, name='logout'),
    path('reset_password1/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name = "password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]