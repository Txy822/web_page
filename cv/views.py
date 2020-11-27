
from django.shortcuts import render
from django.utils import timezone
from .models import Cv_section
from django.shortcuts import render, get_object_or_404
from .forms import Cv_section_form
from django.shortcuts import redirect



def cv_section_list(request):
    cv_sections = Cv_section.objects.all()
    return render(request, 'cv/cv_section_list.html', {'cv_sections': cv_sections})

def cv_section_detail(request, pk):
    cv_section = get_object_or_404(Cv_section, pk=pk)
    return render(request, 'cv/cv_section_detail.html', {'cv_section': cv_section})

def cv_section_new(request):
    if request.method == "POST":
        form = Cv_section_form(request.POST)
        if form.is_valid():
            cv_section = form.save(commit=False)
            cv_section.save()
            return redirect('cv_section_detail', pk=cv_section.pk)
    else:
        form = Cv_section_form()
    return render(request, 'cv/cv_section_edit.html', {'form': form})


def cv_section_edit(request, pk):
    cv_section = get_object_or_404(Cv_section, pk=pk)
    if request.method == "POST":
        form = Cv_section_form(request.POST, instance=cv_section)
        if form.is_valid():
            cv_section = form.save(commit=False)
            cv_section.save()
            return redirect('cv_section_detail', pk=cv_section.pk)
    else:
        form = Cv_section_form(instance=cv_section)
    return render(request, 'cv/cv_section_edit.html', {'form': form})


def cv_section_remove(request, pk):
    cv_section = get_object_or_404(Cv_section, pk=pk)
    cv_section.delete()
    return redirect('cv_section_list')
