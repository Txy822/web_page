
from django.shortcuts import render
from django.utils import timezone
from .models import Cv
from django.shortcuts import render, get_object_or_404
from .forms import CvForm
from django.shortcuts import redirect


def cv_list(request):
    cvs = Cv.objects.all()
    return render(request, 'cv/cv_list.html', {'cvs': cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(Cv, pk=pk)
    return render(request, 'cv/cv_detail.html', {'cv': cv})


def cv_new(request):
    if request.method == "POST":
        form = CvForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
           # post.published_date = timezone.now()
            cv.save()
            return redirect('cv_detail', pk=cv.pk)
    else:
        form = CvForm()
    return render(request, 'cv/cv_edit.html', {'form': form})


def cv_edit(request, pk):
    cv = get_object_or_404(Cv, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)

            # post.published_date = timezone.now()
            cv.save()
            return redirect('cv_detail', pk=cv.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form})


def cv_remove(request, pk):
    cv = get_object_or_404(Cv, pk=pk)
    cv.delete()
    return redirect('cv_list')
