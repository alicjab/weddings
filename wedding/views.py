#-*- coding: utf-8 -*-

from django.shortcuts import render

from .models import Gift

def gift_list(request):
    new_gifts = Gift.objects.filter(accepted=False)
    accepted_gifts = Gift.objects.filter(accepted=True)
    return render(request, 'wedding/gift_list.html', {'new_gifts' : new_gifts, 'accepted_gifts' : accepted_gifts})
