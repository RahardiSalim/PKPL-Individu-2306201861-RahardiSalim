from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'nomor_hp', 'tanggal_lahir')
