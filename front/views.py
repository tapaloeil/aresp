from django.shortcuts import render

# Create your views here.
def animal_list(request):
    return render(request, 'front/animal_list.html',{})