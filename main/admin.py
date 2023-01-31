from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Person, News, Gallery


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created', 'is_public', )
    list_filter = ('is_public', )


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created', 'is_public', )
    list_filter = ('is_public', )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialist', )


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', )


admin.site.register(Post, PostAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(Group)
