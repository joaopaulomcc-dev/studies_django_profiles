from django.urls import path
from pages.views import home_view, profile_view

app_name = "pages"

urlpatterns = [
    path("", home_view, name="home"),
    path(
        "<str:username>",
        profile_view,
        name="profile",
    ),
]
