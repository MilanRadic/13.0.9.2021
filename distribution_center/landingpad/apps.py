from django.apps import AppConfig
#from django.core.mail import send_mail

#send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)

class LandingpadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landingpad'
