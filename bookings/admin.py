from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        # "kind",
        "user",
        "created_at",
    )
    # list_filter = ("kind",)