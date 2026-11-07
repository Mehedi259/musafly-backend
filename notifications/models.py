from django.db import models
from django.utils import timezone

class NotificationCampaign(models.Model):
    TARGET_TYPE_CHOICES = [
        ('all', 'সকল ইউজার (সাধারণ)'),
        ('flight', 'ফ্লাইট বুকিং (Flight)'),
        ('umrah', 'ওমরাহ প্যাকেজ (Umrah)'),
        ('visa', 'ভিসা সার্ভিস (Visa)'),
        ('tour', 'ট্যুর প্যাকেজ (Tour)'),
        ('deal', 'হট ডিল (Hot Deal)'),
        ('external_url', 'ওয়েবসাইট লিংক (URL)'),
    ]

    title = models.CharField(max_length=255, help_text="নোটিফিকেশন টাইটেল")
    message = models.TextField(help_text="নোটিফিকেশনের বিস্তারিত মেসেজ")
    image = models.ImageField(upload_to="notifications/", blank=True, null=True, help_text="ব্যানার ছবি")
    badge_text = models.CharField(max_length=50, default="বিশেষ অফার", blank=True, null=True)
    target_type = models.CharField(max_length=50, choices=TARGET_TYPE_CHOICES, default='all')
    target_id = models.CharField(max_length=255, blank=True, null=True, help_text="নির্দিষ্ট প্যাকেজ বা ফ্লাইটের আইডি (যদি থাকে)")
    external_link = models.URLField(blank=True, null=True, help_text="এক্সটার্নাল ওয়েবসাইট লিংক")
    is_active = models.BooleanField(default=True)
    sent_count = models.IntegerField(default=0, help_text="কতজন ইউজারের কাছে পুশ পাঠানো হয়েছে")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class DeviceToken(models.Model):
    PLATFORM_CHOICES = [
        ('android', 'Android'),
        ('ios', 'iOS'),
        ('web', 'Web'),
    ]

    token = models.CharField(max_length=500, unique=True, help_text="FCM Device Registration Token")
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES, default='android')
    user_email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.platform} - {self.token[:20]}... ({self.user_email or 'Guest'})"


class AppUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=1000, blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_login']

    def __str__(self):
        return f"{self.name} ({self.email})"

