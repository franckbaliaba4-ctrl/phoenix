from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.views.generic import TemplateView
import json


# In gallery_app/views.py:
import os
from django.shortcuts import render
from django.conf import settings





def rex(request):
    # Données statiques pour la modale
    pdg_message = "Ceci est un message inspirant du PDG pour l'équipe Phoenix Group."
    photo_url = "static/img/about-company-1.jpg"  # Chemin vers l'image
    speech = "Je suis fier de diriger cette équipe vers de nouveaux horizons. Ensemble, nous réussirons !"

    context = {
        'pdg_message': pdg_message,
        'photo_url': photo_url,
        'speech': speech,
    }
    return render(request, 'rex.html', context)


def phoenix_group(request):
    subsidiaries = [
        {
            'name': 'Phoenix Express Service',
            'description': 'Une filiale de Phoenix Group offrant des services de transport rapides et fiables.',
            'url': 'https://www.phoenixexpressservice.com'  # Remplacez par l'URL réelle
        },
        {
            'name': 'Blue Sky Technology',
            'description': 'Une entreprise innovante spécialisée dans les solutions technologiques.',
            'url': 'https://www.blueskytechnology.com'  # Remplacez par l'URL réelle
        },
    ]

    context = {
        'subsidiaries': subsidiaries,
    }
    return render(request, 'phoenix_group.html', context)


def send_contact_email(request, name, email, subject, message):
    subject = f"[Contact] {subject} - {name}"

    email_message = render_to_string("emails/email-template.txt", {
        'message': message,
        'email': email,
        'name': name,
    })

    try:
        # Send message
        send_mail(
            subject=subject,
            message=email_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return True
    except Exception:
        return False


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"


def index(request):
    subsidiaries = [
        {
            'name': 'Phoenix Express Service',
            'description': 'Une filiale de Phoenix Group offrant des services de transport rapides et fiables.',
            'url': 'https://www.phoenixexpressservice.com'
        },
        {
            'name': 'Blue Sky Technology',
            'description': 'Une entreprise innovante spécialisée dans les solutions technologiques.',
            'url': 'https://www.blueskytechnology.com'
        },
    ]
    pdg_message = "Ceci est un message inspirant du PDG pour l'équipe Phoenix Group."
    photo_url = "static/img/about-company-1.jpg"
    speech = "Je suis fier de diriger cette équipe vers de nouveaux horizons. Ensemble, nous réussirons !"

    context = {
        'subsidiaries': subsidiaries,
        'pdg_message': pdg_message,
        'photo_url': photo_url,
        'speech': speech,
    }


    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        if send_contact_email(request, name, email, subject, message):
            return JsonResponse({'success': True, 'message': 'Message envoyé avec succès.'})
        else:
            return JsonResponse({'success': False, 'message': "Erreur lors de l'envoie du message."})
    return JsonResponse({'success': False, 'message': "Méthode non autorisée"}, status=405)


def page404(request, exception):
    return render(request, "404.html")










