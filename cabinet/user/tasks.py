from django.core.mail import mail_admins, send_mail

from cabinet import settings
from cabinet.celery import app


@app.task
def send_email_to_admin(subject, message):
    mail_admins(subject, message)


@app.task
def welcome_email(subject, message, email):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email]
    )
