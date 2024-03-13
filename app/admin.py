from django.contrib import admin

# Register your models here.
from .models import FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')