from django.contrib import admin
from .models import NotificationCampaign, DeviceToken, AppUser

@admin.register(NotificationCampaign)
class NotificationCampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_type', 'badge_text', 'sent_count', 'is_active', 'created_at')
    list_filter = ('target_type', 'is_active', 'created_at')
    search_fields = ('title', 'message')

@admin.register(DeviceToken)
class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ('platform', 'user_email', 'token_snippet', 'is_active', 'updated_at')
    list_filter = ('platform', 'is_active')
    search_fields = ('token', 'user_email')

    def token_snippet(self, obj):
        return f"{obj.token[:25]}..."

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_active', 'last_login')
    search_fields = ('name', 'email', 'phone')

