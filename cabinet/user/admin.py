from django.contrib import admin
from .models import *
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Register your models here.

class UserForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'phone-number'}),
        }

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
