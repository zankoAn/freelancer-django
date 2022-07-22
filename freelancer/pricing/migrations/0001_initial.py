# Generated by Django 4.0.5 on 2022-07-22 07:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_type', models.CharField(max_length=150, verbose_name='نوع پنل(برنزی، نقره ای، طلایی، الماس)')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت پنل به ریال')),
                ('count', models.PositiveSmallIntegerField(default=5, verbose_name='تعداد پیشنهاد های ارسالی در ماه')),
                ('days', models.IntegerField(default=30, verbose_name='تعداد روز های مجاز')),
                ('position', models.PositiveSmallIntegerField(unique=True, verbose_name='موقعیت و جایگاه این پنل در بین پنل ها')),
                ('discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PricingTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='اسم تگ')),
                ('price', models.IntegerField(default=200000, verbose_name='قیمت به ریال')),
            ],
        ),
        migrations.CreateModel(
            name='ActivePricingPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='تعداد پیشنهاد های ارسال شده')),
                ('expire_time', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 7, 23, 46, 195822, tzinfo=utc), verbose_name='تاریخ انقضای پنل')),
                ('active_panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_pricing_panel', to='pricing.pricingpanel', verbose_name='پنل فعال')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pricing_panel', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]
