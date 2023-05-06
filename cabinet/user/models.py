from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(_("email address"),unique=True)
    name_and_surname = models.CharField('Фамилия и имя', max_length=150)
    address = models.CharField("Адрес", max_length=355)
    postcode = models.PositiveIntegerField(default=1234567)
    phone_number = PhoneNumberField()
    city = models.CharField("Город", max_length=255)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
