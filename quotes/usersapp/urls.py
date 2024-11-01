from django.urls import path
from usersapp import views
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


app_name = "usersapp"

urlpatterns = [
    path("signup/", views.signupuser, name="signup"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("reset-password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "reset-password/done/",
        PasswordResetDoneView.as_view(
            template_name="usersapp/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="usersapp/password_reset_confirm.html",
            success_url="/usersapp/reset-password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="usersapp/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
