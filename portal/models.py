from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html


class News(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["created_date"]
        verbose_name_plural = "News"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])

# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('author','title','created_date','published_date')


class Videos(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    GENRE_CHOICES = [
        ('REV', 'Review'),
        ('SCI', 'Science'),
        ('HUM', 'Humor'),
    ]

    genre = models.CharField(
        max_length=3,
        choices=GENRE_CHOICES,
        default='REV',
    )

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["created_date"]
        verbose_name_plural = "Videos"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
