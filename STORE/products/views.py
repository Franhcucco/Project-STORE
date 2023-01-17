from django.shortcuts import render
from django.http import HttpResponse

from products.models import *
from products.forms import *

def shoes_list (request):  
    all = shoes.objects.all()
    print(all)
    context = {
        'shoes':all,
    }
    return render(request, 'shoes_list.html', context=context)

def tshirts_list (request):  
    all = tShirt.objects.all()
    print(all)
    context = {
        'tShirts':all,
    }
    return render(request, 'tshirts_list.html', context=context)

def pants_list (request):  
    all = pants.objects.all()
    print(all)
    context = {
        'pants':all,
    }
    return render(request, 'pants_list.html', context=context)

def products_list (request):
    if 'search' in request.GET:
        search = request.GET['search']
        p = pants.objects.filter(name__icontains=search)
        t = tShirt.objects.filter(name__icontains=search)
        s = shoes.objects.filter(name__icontains=search)
    else:
        p = pants.objects.all()
        t = tShirt.objects.all()
        s = shoes.objects.all()
    context = {
         'p': p,
         't' : t,
         's' : s,
    }
    return render(request, 'products_list.html', context=context)

def create_pants(request):
    if request.method == 'GET':
        context={
            'form' : PantsForm()
        }

        return render(request, 'create_pants.html', context=context)

    elif request.method == 'POST':
        form = PantsForm(request.POST)
        if form.is_valid():
            pants.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                size = form.cleaned_data['size'],
                stock = form.cleaned_data['stock'],
            )
            return render(request, 'create_pants.html', context={})
        else:
            context = {
                'form_errors' : form.errors,
                'form' : PantsForm()
            }
            return render(request, 'create_pants.html', context=context)

def create_tshirts(request):
    if request.method == 'GET':
        context={
            'form' : TshirtForm()
        }

        return render(request, 'create_tshirts.html', context=context)

    elif request.method == 'POST':
        form = TshirtForm(request.POST)
        if form.is_valid():
            tShirt.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                size = form.cleaned_data['size'],
                stock = form.cleaned_data['stock'],
            )
            return render(request, 'create_tshirts.html', context={})
        else:
            context = {
                'form_errors' : form.errors,
                'form' : TshirtForm()
            }
            return render(request, 'create_tshirts.html', context=context)

def create_shoes(request):
    if request.method == 'GET':
        context={
            'form' : ShoesForm()
        }

        return render(request, 'create_shoes.html', context=context)

    elif request.method == 'POST':
        form = ShoesForm(request.POST)
        if form.is_valid():
            shoes.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                size = form.cleaned_data['size'],
                stock = form.cleaned_data['stock'],
            )
            return render(request, 'create_shoes.html', context={})
        else:
            context = {
                'form_errors' : form.errors,
                'form' : ShoesForm()
            }
            return render(request, 'create_shoes.html', context=context)