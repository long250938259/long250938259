from django.contrib import admin
from django.contrib import admin
from blog.models import BookInfo
from blog.models import HeroInfo
from blog.models import People
from .models import Post

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
admin.site.register(People)

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)