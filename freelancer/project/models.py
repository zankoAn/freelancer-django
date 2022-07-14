import uuid

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify
from django_quill.fields import QuillField
from django.core.validators import MaxValueValidator, MinValueValidator



class Category(models.Model):
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        verbose_name='زیردسته',
        related_name='children')
    
    name = models.CharField(
        max_length=200,
        verbose_name='عنوان دسته')
    
    slug = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='آدرس دسته')
    
    status = models.BooleanField(
        default=True,
        verbose_name='فعال شود ؟')
    
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    User = get_user_model()

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user_project")
    
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='category_project')

    title = models.CharField(
        max_length=60,
        verbose_name="عنوان پروژه")
        
    slug = models.SlugField(
        max_length=120,
        blank=True,
        null=True,
        default=None,
        allow_unicode=True)

    tags = ArrayField(
        models.CharField(
            max_length=30,
            blank=True,
            null=True),
        blank=True,
        null=True,
        size=5,
        verbose_name="تگ های پروژه")

    description = QuillField(
        max_length=20000,
        verbose_name='توضیحات پروژه')

    status = models.BooleanField(
        default=False,
        verbose_name="وضعیت تموم شدن پروژه")

    budget = models.CharField(
        max_length=100,
        verbose_name="بودجه")

    urgent = models.BooleanField(
        default=False,
        verbose_name="فوری")

    highlight = models.BooleanField(
        default=False,
        verbose_name="برجسته")
    
    private = models.BooleanField(
        default=False,
        verbose_name="محرمانه")

    paid = models.BooleanField(
        default=False,
        verbose_name="پرداخت شده؟")

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True)

    created = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        """
            Create a new job with a 'Persian' dynamic slug.
        """
        self.slug = slugify(value=self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_tags(self):
        return " ,".join(self.tags)


class ApplyProject(models.Model):
    APPLY_STATUS_CHOICES = (
        ('accept', 'پذیرفته شد'),
        ('reject', 'رد شد'),
        ('wait', 'در حال انتظار')
    )

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="user_project_applay")

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="project_applay")

    status = models.CharField(
        max_length=20,
        choices=APPLY_STATUS_CHOICES,
        verbose_name='وضعیت درخواست',
        default='wait')

    description = models.TextField(
        max_length=500,
        verbose_name='توضیحات برای کارفرما')

    bid_amount = models.CharField(
        max_length=100,
        default=0,
        verbose_name="مبلغ پیشنهادی")

    bid_date = models.IntegerField(
        default=0,
        verbose_name="زمان انجام پروژه")

    created = models.DateTimeField(auto_now=True)


class EmployersComment(models.Model):
    to = models.OneToOneField(
        ApplyProject, 
        on_delete=models.CASCADE, 
        related_name='comment_to', 
        unique=True)

    star = models.IntegerField(
        default=0,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)])

    comment = models.TextField(max_length=150)