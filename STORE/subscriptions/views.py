from django.http import HttpResponse
from django.shortcuts import render

from subscriptions.models import *
from subscriptions.forms import *

# Create your views here.

def subscription(request):
    if request.method == 'GET':
        context={
            'form' : SubscriptionForm()
        }

        return render(request, 'create_subscription.html', context=context)

    elif request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriptions.objects.create(
                name = form.cleaned_data['name'],
                mail = form.cleaned_data['mail'],
            )
            return render(request, 'create_subscription.html', context={})
        else:
            context = {
                'form_errors' : form.errors,
                'form' : SubscriptionForm()
            }
            return render(request, 'create_subscription.html', context=context)