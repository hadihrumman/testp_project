from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def landing(request):
    name = "hadi"
    current_day = "24.12.2017"
    form =SubscriberForm(request.POST or None)


    if request.method =="POST" and form.is_valid():
        print (request.POST)
        print(form.cleaned_data)
        data =form.cleaned_data

        print(form.cleaned_data['name'])
        print(data['name'])

        new_form = form.save()



    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())