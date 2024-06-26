from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "top_fixed",
        "created_at",
    )