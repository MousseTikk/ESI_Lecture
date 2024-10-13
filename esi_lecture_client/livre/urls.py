from django.urls import path
from . import views

app_name = 'livre'
urlpatterns = [
    path('', views.livre, name='livre'),
    path('like/<int:book_id>/', views.like_book, name='like'),
]