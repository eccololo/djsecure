from django.urls import path
from . import views

# Password Management
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("user-logout", views.user_logout, name="user-logout"),
    path("account-locked", views.account_locked, name="account-locked"),
    # Password Management Urls/Views
    
    # If doesn't work change in names - to _.
    # 1. Submit email for reseting password.
    path("reset_password", auth_views.PasswordResetView.as_view(template_name="password-reset/password-reset.html"), name="reset_password"),

    # 2. Success message - reset password email was send successfuly.
    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name="password-reset/password-reset-sent.html"), name="password_reset_done"),
   
    # 3. Send link to given email to reset password.
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password-reset/password-reset-form.html"), name="password_reset_confirm"),

    # 4. Show success message that password was changed.
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name="password-reset/password-reset-complete.html"), name="password_reset_complete") 
]
