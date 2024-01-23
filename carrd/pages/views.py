from django.shortcuts import render


def home_view(request):
    response = render(request, "pages/index.html")
    return response
