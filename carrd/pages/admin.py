from django.contrib import admin
from pages.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "text"]


admin.site.register(Profile, ProfileAdmin)
