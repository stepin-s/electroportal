from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import News
from .forms import NewsForm
from .models import Videos
from .forms import VideosForm


def news_list(request):
    news = News.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
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


def videos_list(request):
    videos = Videos.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portal/videos_list.html', {'videos': videos})


def video_detail(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    return render(request, 'portal/video_detail.html', {'video': video	})

def video_add(request):
    if request.method == "POST":
        form = VideosForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.published_date = timezone.now()
            video.save()
            return redirect('videos_list', pk=video.pk)
    else:
        form = VideosForm()
    return render(request, 'portal/video_edit.html', {'form': form})

def video_edit(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    if request.method == "POST":
        form = VideosForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.published_date = timezone.now()
            video.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideosForm(instance=video)
    return render(request, 'portal/video_edit.html', {'form': form})