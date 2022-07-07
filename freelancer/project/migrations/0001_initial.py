# Generated by Django 4.0.5 on 2022-07-07 13:48

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='عنوان پروژه')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default=None, max_length=120, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, null=True, size=5, verbose_name='تگ های پروژه')),
                ('description', django_quill.fields.QuillField(max_length=20000, verbose_name='توضیحات پروژه')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت تموم شدن پروژه')),
                ('budget', models.CharField(max_length=100, verbose_name='بودجه')),
                ('urgent', models.BooleanField(default=False, verbose_name='فوری')),
                ('highlight', models.BooleanField(default=False, verbose_name='برجسته')),
                ('private', models.BooleanField(default=False, verbose_name='محرمانه')),
                ('paid', models.BooleanField(default=False, verbose_name='پرداخت شده؟')),
                ('created', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_project', to='job.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accept', 'پذیرفته شد'), ('reject', 'رد شد'), ('wait', 'در حال انتظار')], default='wait', max_length=20, verbose_name='وضعیت درخواست')),
                ('description', models.TextField(max_length=500, verbose_name='توضیحات برای کارفرما')),
                ('bid_amount', models.CharField(default=0, max_length=100, verbose_name='مبلغ پیشنهادی')),
                ('bid_date', models.IntegerField(default=0, verbose_name='زمان انجام پروژه')),
                ('created', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_applay', to='project.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project_applay', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
