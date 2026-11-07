# Generated for notifications app

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='নোটিফিকেশন টাইটেল', max_length=255)),
                ('message', models.TextField(help_text='নোটিফিকেশনের বিস্তারিত মেসেজ')),
                ('image', models.ImageField(blank=True, help_text='ব্যানার ছবি', null=True, upload_to='notifications/')),
                ('badge_text', models.CharField(blank=True, default='বিশেষ অফার', max_length=50, null=True)),
                ('target_type', models.CharField(choices=[('all', 'সকল ইউজার (সাধারণ)'), ('flight', 'ফ্লাইট বুকিং (Flight)'), ('umrah', 'ওমরাহ প্যাকেজ (Umrah)'), ('visa', 'ভিসা সার্ভিস (Visa)'), ('tour', 'ট্যুর প্যাকেজ (Tour)'), ('deal', 'হট ডিল (Hot Deal)'), ('external_url', 'ওয়েবসাইট লিংক (URL)')], default='all', max_length=50)),
                ('target_id', models.CharField(blank=True, help_text='নির্দিষ্ট প্যাকেজ বা ফ্লাইটের আইডি (যদি থাকে)', max_length=255, null=True)),
                ('external_link', models.URLField(blank=True, help_text='এক্সটার্নাল ওয়েবসাইট লিংক', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('sent_count', models.IntegerField(default=0, help_text='কতজন ইউজারের কাছে পুশ পাঠানো হয়েছে')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(help_text='FCM Device Registration Token', max_length=500, unique=True)),
                ('platform', models.CharField(choices=[('android', 'Android'), ('ios', 'iOS'), ('web', 'Web')], default='android', max_length=30)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('photo_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('google_id', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-last_login'],
            },
        ),
    ]

