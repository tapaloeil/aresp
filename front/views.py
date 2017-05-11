from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Animal

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'front/animal_list.html',{'animals':animals})

def animal_detail(request,pk):
	animal=get_object_or_404(Animal, pk=pk)
	return render(request, 'front/animal_detail.html',{'animal':animal})