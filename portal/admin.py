from django.contrib import admin
from .models import News
from .models import Videos

admin.site.register(Videos)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'created_date', 'published_date')


admin.site.register(News, NewsAdmin)
