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


def modify_page(request, id):
    carid = Cars.objects.get(id=id)
    context = {'car': carid}
    if request.method == 'POST':
        car_name = request.POST.get('carname')
        car_desc = request.POST.get('car_desc')
        car_image = request.FILES.get('image')

        carid.carname = car_name
        carid.cardesc = car_desc
        carid.carimage = car_image

        carid.save()

        return redirect('/main/')

    return render(request, 'main/modify.html', context)


def delete_car(request, id):
    car = Cars.objects.get(id=id)
    car.delete()
    return redirect('/main/')
