from django.contrib import admin
from .models import News
from .models import Videos

admin.site.register(News),
admin.site.register(Videos)