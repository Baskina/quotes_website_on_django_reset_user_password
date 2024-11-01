from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView

from usersapp.forms import UserRegisterForm, UserLoginForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotesapp:main")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "usersapp/signupuser.html", {"form": form})
    return render(
        request, "usersapp/signupuser.html", context={"form": UserRegisterForm()}
    )


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotesapp:main")

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            return redirect(to="usersapp:loginuser")

        login(request, user)
        return redirect(to="quotesapp:main")

    return render(request, "usersapp/loginuser.html", context={"form": UserLoginForm()})


@login_required()
def logoutuser(request):
    logout(request)
    return redirect(to="quotesapp:main")


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "usersapp/password_reset.html"
    email_template_name = "usersapp/password_reset_email.html"
    html_email_template_name = "usersapp/password_reset_email.html"
    success_url = reverse_lazy("usersapp:password_reset_done")
    success_message = (
        "An email with instructions to reset your password has been sent to %(email)s."
    )
    subject_template_name = "usersapp/password_reset_subject.txt"
