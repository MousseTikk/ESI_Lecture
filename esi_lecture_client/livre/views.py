from django.shortcuts import render, redirect
from django.conf import settings
import xmlrpc.client
from django.contrib import messages
import functools


def livre(request):
    if request.session['is_connected']:
        username = request.session['username']
        password = request.session['password']

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(settings.URL_ODOO))  
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(settings.URL_ODOO))
        uid = common.authenticate(settings.DB_ODOO, username, password, {})    


        search_domain = [[]]
        print(request.POST.get('book_name_search'))
        if request.POST.get('book_name_search') != None:
            search_domain = [[['name', 'ilike', request.POST.get('book_name_search')]]]

        search_options = {
            'fields': ['name', 'description', 'date_publication', 'nombre_page', 'likes_count', 'auteur_ids', 'liked_by_users', 'couverture_image'],
            'order': 'likes_count desc, name asc'
        }

        books = models.execute_kw(settings.DB_ODOO, uid, password, 'livre.livre', 'search_read', search_domain, search_options)

        books = sorted(books, key=functools.cmp_to_key(lambda x, y: (y['likes_count'] - x['likes_count']) or (x['name'] < y['name'])))

        authors = models.execute_kw(settings.DB_ODOO, uid, password, 'res.partner', 'search_read', [[('category_id', 'ilike', 'Auteur')], ['name']])
        for book in books:
            author_names = [author['name'] 
                            for author in authors 
                                if author['id'] in book['auteur_ids']]
            book['auteur_names'] = author_names

        for book in books:
            book['is_liked'] = False
            for liked_by_user in book['liked_by_users']:
                if uid == liked_by_user:
                    book['is_liked'] = True
                    break
               
        context = {
            'books': books,
            'search': request.POST.get('book_name_search'),
        }

        return render(request, 'livre/livre.html', context)
    else:
        messages.error(request, 'Authentification échouée. Vérifiez votre login et/ou mot de passe.')
        return redirect('connexion:odoo_login')


def like_book(request, book_id):
    if request.session['is_connected']:
        username = request.session['username']
        password = request.session['password']

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(settings.URL_ODOO))  
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(settings.URL_ODOO))

        uid = common.authenticate(settings.DB_ODOO, username, password, {})

        result = models.execute_kw(settings.DB_ODOO, uid, password, 'livre.livre', 'toggle_like', [int(book_id)])
        
        if result:
            messages.success(request, 'liké / déliké')
        else:
            messages.error(request, 'Erreur lors de la mise à jour des likes')

        return redirect('livre:livre') 

    else:
        messages.error(request, 'Vous devez être connecté.')
        return redirect('connexion:odoo_login')
