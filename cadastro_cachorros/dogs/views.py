from django.shortcuts import render, redirect
from .models import Dog
from .forms import DogForm
from .forms import BreedForm

def dog_list(request):
    dogs = Dog.objects.all()
    form = DogForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dog_list')

    return render(request, 'dogs/dog_list.html', {'dogs': dogs, 'form': form})



def breed_create(request):
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dogs:breed_list')
    else:
        form = BreedForm()
    return render(request, 'dogs/breed_create.html', {'form': form})