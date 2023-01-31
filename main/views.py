from django.shortcuts import render, get_object_or_404
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


def person(request):
    all_person = Person.objects.filter()

    return render(request, 'main/teaching/person/person.html', {'all_person': all_person})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    return render(request, 'main/teaching/person/person_detail.html', {'person': person})


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


# Жаңалықтар
def news(request):
    all_news = News.objects.filter(is_public=True)

    return render(request, 'main/news/news.html', {'all_news': all_news})


def news_detail(request, pk):
    new_detail = get_object_or_404(News, pk=pk)

    return render(request, 'main/news/news_detail.html', {'new_detail': new_detail})


# Мақалалар
def articles(request):
    posts = Post.objects.filter(is_public=True)

    return render(request, 'main/articles/articles.html', {'posts': posts})


def article_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/articles/article_detail.html', {'post': post})


# Балалар бөлімі
def children(request):
    return render(request, 'main/children.html', {})


# Медиагалерея
def mediagallery(request):
    galleries = Gallery.objects.filter()
    return render(request, 'main/mediagallery.html', {'galleries': galleries})
