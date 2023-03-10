from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('historic/', views.historic, name='historic'),
    path('legacy/', views.legacy, name='legacy'),
    path('reviews/', views.reviews, name='reviews'),
    path('books/', views.books, name='books'),


    path('mausoleum/', views.mausoleum, name='mausoleum'),
    path('person/', views.person, name='person'),
    path('person_detail/<pk>/', views.person_detail, name='person_detail'),

    path('department_of_mothers/', views.department_of_mothers, name='department_of_mothers'),


    path('grand_words/', views.grand_words, name='grand_words'),
    path('termes/', views.termes, name='termes'),
    path('songs/', views.songs, name='songs'),
    path('states/', views.states, name='states'),
    path('literature/', views.literature, name='literature'),


    path('chronicle/', views.chronicle, name='chronicle'),


    path('charity/', views.charity, name='charity'),
    path('news/', views.news, name='news'),
    path('news/<pk>/', views.news_detail, name='news_detail'),

    path('articles/', views.articles, name='articles'),
    path('articles/<pk>/', views.article_detail, name='article_detail'),

    path('children/', views.children, name='children'),
    path('mediagallery/', views.mediagallery, name='mediagallery'),

]
