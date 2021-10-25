from django.shortcuts import render
from django.core.mail import send_mail
from contact.models import ContactInfo
from django.conf import settings

# Create your views here.


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        # print(subject)
        # print(email)
        # print(message)

    return render(request, "contact/contact.html", {'title': 'Contact Us',
                                                    'Contact_info': ContactInfo.objects.get(id='1')})
