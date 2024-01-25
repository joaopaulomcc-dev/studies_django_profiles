import random

from django.shortcuts import render
from pages.models import Profile


def home_view(request):
    profiles = Profile.objects.all()

    context = {}

    if len(profiles) < 10:
        context["profiles"] = profiles
    else:
        context["profiles"] = random.sample(profiles, 10)

    response = render(request, "pages/index.html", context)

    return response


def profile_view(request, username):
    try:
        profile_obj = Profile.objects.get(user__username=username)

    except Profile.DoesNotExist:
        return render(request, "pages/profile_not_found.html", {"username": username})

    paragraphs = profile_obj.text.split("\n")

    context = {
        "profile_owner_full_name": profile_obj.user.get_full_name(),
        "paragraphs": paragraphs,
    }

    return render(request, "pages/profile.html", context)
