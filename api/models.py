from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from api.utilities import get_timestamp_path


class Organization(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Организация', db_index=True)
    description = models.TextField(max_length=250)
    address = models.TextField(max_length=90)
    postcode = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['-title']


class AdvUser(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    email = models.EmailField('email.', unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta(AbstractUser.Meta):
        pass


class Event(models.Model):
    title = models.CharField(max_length=60, verbose_name='Мероприятие', db_index=True)
    description = models.TextField(max_length=250, verbose_name='Описание')
    organizations = models.ManyToManyField(AdvUser, db_index=True, blank=False)
    image = models.ImageField(blank=True, upload_to=get_timestamp_path,
                              verbose_name='Изображение')
    date = models.DateTimeField(db_index=True, blank=False, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
