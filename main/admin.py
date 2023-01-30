from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created', 'is_public', )
    list_filter = ('is_public', )


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)
