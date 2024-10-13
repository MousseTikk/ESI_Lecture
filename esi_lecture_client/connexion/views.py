from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import xmlrpc.client
from django.conf import settings



def connexion(request):

    return render(request, 'connexion/connexion.html')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
    if not username or not password:
        messages.error(request, 'Veuillez remplir tous les champs du formulaire.')
        return render(request, 'connexion/connexion.html')

    try:
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(settings.URL_ODOO))  

        uid = common.authenticate(settings.DB_ODOO, username, password, {})

        if uid is False:
            messages.error(request, 'Authentification échouée. Vérifiez votre login et/ou mot de passe.')
            return render(request, 'connexion/connexion.html')
        else:
            print(username, password)
            request.session['is_connected'] = True
            request.session['username'] = username
            request.session['password'] = password
            messages.success(request, 'Authentification réussie')

    except Exception as e:
        messages.error(request, 'Problème avec la connexion au serveur Odoo.')
        return render(request, 'connexion/connexion.html')
    

    return HttpResponseRedirect(reverse('home:home'))



def logout(request):

    request.session['is_connected'] = False

    return HttpResponseRedirect(reverse('home:home'))

# Create your views here.
