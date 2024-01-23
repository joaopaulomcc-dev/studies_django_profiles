from accounts.views import SignUpView
from django.urls import path

app_name = "accounts"


urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
]
