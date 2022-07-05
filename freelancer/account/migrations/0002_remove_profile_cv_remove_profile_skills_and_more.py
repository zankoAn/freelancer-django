# Generated by Django 4.0.5 on 2022-07-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تلفن کاربر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.ImageField(default=0, upload_to='', verbose_name='امتیاز کاربر'),
        ),
    ]