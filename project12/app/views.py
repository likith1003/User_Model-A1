from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.


def register(request):
    EUFO = UserForm()
    d = {'EUFO': EUFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.is_staff = True
            MUFDO.is_superuser = True
            MUFDO.save()
            return HttpResponse('Done....')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)