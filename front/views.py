from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Animal
from .forms import AnimalForm

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'front/animal_list.html',{'animals':animals})

def animal_detail(request,pk):
	animal=get_object_or_404(Animal, pk=pk)
	return render(request, 'front/animal_detail.html',{'animal':animal})

def animal_new(request):
	if request.method == "POST":
		form=AnimalForm(request.POST)
		if form.is_valid():
			animal=form.save(commit=False)
			animal.user_ajout=request.user
			animal.publier()
			animal.save()
			return redirect('animal_detail', pk=animal.pk)
	else:
		form=AnimalForm()
	return render(request, 'front/animal_edit.html',{'form':form})

def animal_edit(request, pk):
	animal=get_object_or_404(Animal, pk=pk)
	if request.method=="POST":
		form=AnimalForm(request.POST, instance=animal)
		if form.is_valid():
			animal=form.save(commit=False)
			animal.publier()
			animal.save()
			return redirect('animal_detail', pk=animal.pk)
	else:
		form=AnimalForm(instance=animal)
	return render(request, 'front/animal_edit.html',{'form':form})