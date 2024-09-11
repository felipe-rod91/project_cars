from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    print(request.GET.get('search'))
    print(request.GET.get('nome'))
    cars = Car.objects.all()

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )
