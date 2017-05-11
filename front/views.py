from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Animal
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'front/animal_list.html',{'animals':animals})

@login_required
def animal_draft_list(request):
    animals = Animal.objects.filter(date_publication__isnull=True).order_by('date_ajout')
    return render(request, 'front/animal_draft_list.html',{'animals':animals})

def animal_detail(request,pk):
	animal=get_object_or_404(Animal, pk=pk)
	return render(request, 'front/animal_detail.html',{'animal':animal})

@login_required
def animal_new(request):
	if request.method == "POST":
		form=AnimalForm(request.POST)
		if form.is_valid():
			animal=form.save(commit=False)
			animal.user_ajout=request.user
			animal.save()
			return redirect('animal_detail', pk=animal.pk)
	else:
		form=AnimalForm()
	return render(request, 'front/animal_edit.html',{'form':form})

@login_required
def animal_edit(request, pk):
	animal=get_object_or_404(Animal, pk=pk)
	if request.method=="POST":
		form=AnimalForm(request.POST, instance=animal)
		if form.is_valid():
			animal=form.save(commit=True)
			return redirect('animal_detail', pk=animal.pk)
	else:
		form=AnimalForm(instance=animal)
	return render(request, 'front/animal_edit.html',{'form':form})

@login_required
def animal_publier(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.publier()
    return redirect('animal_detail', pk=pk)

@login_required
def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    return redirect('animal_list')