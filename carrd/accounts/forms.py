from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User

        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
