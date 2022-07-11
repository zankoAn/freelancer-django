# Generated by Django 4.0.5 on 2022-07-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='educational_level',
            field=models.CharField(choices=[('no_matter', 'مهم نیست'), ('diploma', 'دیپلم'), ('lisanse', 'لیسانس'), ('mastersdegree', 'فوق لیسانس'), ('phd', 'دکترا و بالاتر')], default='no_matter', max_length=30, verbose_name='مدرک تحصیلی'),
        ),
        migrations.AlterField(
            model_name='job',
            name='gender',
            field=models.CharField(choices=[('no_matter', 'مهم نیست'), ('man', 'اقا'), ('femail', 'خانوم')], default='no_matter', max_length=30, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='job',
            name='military_status',
            field=models.CharField(choices=[('end_Soldeir', 'پایان خدمت'), ('soldier', 'در حال انجام'), ('exempt', 'معافیت'), ('included', 'مشمول'), ('no_matter', 'مهم نیست')], default='no_matter', max_length=30, verbose_name='نظام وظیفه'),
        ),
    ]