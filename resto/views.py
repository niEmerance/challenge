from __future__ import unicode_literals
from .forms import RestaurantForm
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render,redirect
from .models import Restaurant

# Create your views here.
def welcome(request):
    try:
        restaurants= Restaurant.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'welcome.html',{"restaurants":restaurants})

def new_restaurant(request):
    current_user = request.user
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.resto_uploader = current_user
            post.save()
        return redirect('welcome')

    else:
        form = RestaurantForm()
    return render(request, 'new_restaurant.html', {"form": form})

def restaurantDetails(request):
    restaurant=Restaurant.objects.all()
    return render(request,'restoDetails.html',{"restaurant":restaurant})
