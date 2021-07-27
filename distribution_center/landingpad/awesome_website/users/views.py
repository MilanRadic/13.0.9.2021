from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm

from django.core.mail import EmailMessage #


def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            user.is_active=False #

            user = form.save()

            email_subject = 'Activate your account' #
            email_body = 'Test body'
            email = EmailMessage( #
                email_subject,
                email_body,
                'noreply@semycolon.com',
                [email],
                ['bcc@example.com'],
            ) #

            email.send(fail_silently=False) #


            login(request, user)
            return redirect(reverse("dashboard"))





