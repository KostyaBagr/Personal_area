from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.core.mail import send_mail, mail_admins
from phonenumber_field.phonenumber import to_python
from cabinet import settings
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'user/cabinet.html')

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('user:index')


class Registration(CreateView):
    template_name = 'user/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user:login')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['region'] = [(code, name) for code, name in to_python(None).phone_number.get_choices()]
    #     return context
    def form_valid(self, form):
        response = super().form_valid(form)

        message = render_to_string('user/email_template.html', {
            'name_and_surname': self.object.name_and_surname,
            'email': self.object.email,
            'address': self.object.address,
            'postcode': self.object.postcode,
            'phone_number': self.object.phone_number,
            'time_created': self.object.time_created,
            'city':self.object.city
        })

        # отправка письма администратору
        subject = 'Новый пользователь зарегистрирован'
        mail_admins(subject, message)
        send_mail(
            'Welcom, your data',
            message,
            settings.EMAIL_HOST_USER,
            [f'{self.object.email}'],
            fail_silently = False,
        )

        return response

