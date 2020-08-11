from django import forms

from .models import News
from .models import Videos

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text',)

class VideosForm(forms.ModelForm):
	
    class Meta:
        model = Videos
        fields = ('title', 'text',)