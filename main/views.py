from django.shortcuts import render
from .models import Post, Person, News, Gallery


# Басты бет
def index(request):
    last_news = News.objects.filter(is_public=True)[:3]
    last_post = Post.objects.filter(is_public=True)[:4]
    person = Person.objects.filter()[:4]
    galleries = Gallery.objects.filter()[:4]

    context = {
        'last_news': last_news,
        'last_post': last_post,
        'person': person,
        'galleries': galleries
    }

    return render(request, 'main/index.html', context)


# Тарихи деректер
# ====================================================================================================================
def historic(request):
    return render(request, 'main/historic/index.html', {})


def legacy(request):
    return render(request, 'main/historic/legacy.html', {})


def reviews(request):
    return render(request, 'main/historic/reviews.html', {})


def books(request):
    return render(request, 'main/historic/books.html', {})


# Тағылымдар
# ====================================================================================================================
def mausoleum(request):
    return render(request, 'main/teaching/mausoleum.html', {})


def persons(request):
    return render(request, 'main/teaching/persons.html', {})


def department_of_mothers(request):
    return render(request, 'main/teaching/department_of_mothers.html', {})


# Руханият
# ====================================================================================================================
def grand_words(request):
    return render(request, 'main/spirituality/grand_words.html', {})


def termes(request):
    return render(request, 'main/spirituality/termes.html', {})


def songs(request):
    return render(request, 'main/spirituality/songs.html', {})


def states(request):
    return render(request, 'main/spirituality/states.html', {})


def literature(request):
    return render(request, 'main/spirituality/literature.html', {})


# Шежіре
# ====================================================================================================================
def chronicle(request):
    return render(request, 'main/chronicle/index.html', {})


# Қайырымдылық
def charity(request):
    return render(request, 'main/charity.html', {})


# Мақалалар
def articles(request):
    return render(request, 'main/articles.html', {})


# Балалар бөлімі
def children(request):
    return render(request, 'main/children.html', {})


# Медиагалерея
def mediagallery(request):
    return render(request, 'main/mediagallery.html', {})