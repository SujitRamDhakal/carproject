from django.shortcuts import render, redirect
from main.models import Cars
# Create your views here.


def main_page(request):
    if request.method == 'POST':
        # data = request.POST
        car_name = request.POST.get('carname')
        car_desc = request.POST.get('car_desc')
        car_image = request.FILES.get('image')

        Cars.objects.create(
            carname=car_name, cardesc=car_desc, carimage=car_image)
        return redirect('/main/')

    cars = Cars.objects.all()
    if request.GET.get('search_car'):
        cars = Cars.objects.filter(
            carname__icontains=request.GET.get('search_car'))
    context = {'cars': cars}
    return render(request, 'main/index.html', context)
