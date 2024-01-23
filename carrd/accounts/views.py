from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
