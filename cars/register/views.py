from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def register_page(request):

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if cpassword == password:
            user = User.objects.create(
                username=username, email=email, first_name=firstname, last_name=lastname)
            user.set_password(password)
            user.save()
        else:
            return HttpResponse("Passwords do not match")

        return redirect('/login/')

    return render(request, 'register/index.html')
