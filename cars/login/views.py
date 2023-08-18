from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
# Create your views here.


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect('/main/')
        else:
            return HttpResponse("username or password error")

    return render(request, 'login/index.html')
