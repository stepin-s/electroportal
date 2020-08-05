from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import News
from .forms import NewsForm

def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portal/news_list.html', {'news': news})

def new_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'portal/new_detail.html', {'new': new})

def new_add(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.published_date = timezone.now()
            new.save()
            return redirect('new_detail', pk=new.pk)
    else:
        form = NewsForm()
    return render(request, 'portal/new_edit.html', {'form': form})

def new_edit(request, pk):
    new = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.published_date = timezone.now()
            new.save()
            return redirect('new_detail', pk=new.pk)
    else:
        form = NewsForm(instance=new)
    return render(request, 'portal/new_edit.html', {'form': form})