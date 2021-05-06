from django.contrib import admin
from django.contrib import admin
from foo.models import BookInfo
from foo.models import HeroInfo
from foo.models import User

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
admin.site.register(User)

# Register your models here.
