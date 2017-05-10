from django.shortcuts import render
from django.utils import timezone
from .models import Animal

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'front/animal_list.html',{'animals':animals})