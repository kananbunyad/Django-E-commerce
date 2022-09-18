from account.tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_email_confirmation(user, current_site):
    subject = 'Activate Your MySite Account'
    message = render_to_string('activation.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # 'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })
    msg = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[settings.EMAIL_HOST_USER], )
    msg.content_subtype = "html"
    msg.send()