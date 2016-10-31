#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


from .models import Gift

def gift_list(request):
    new_gifts = Gift.objects.filter(accepted=False)
    accepted_gifts = Gift.objects.filter(accepted=True)
    return render(request, 'wedding/gift_list.html', {'new_gifts' : new_gifts, 'accepted_gifts' : accepted_gifts})

def gift_detail(request, id):
    gift = get_object_or_404(Gift, id=id)
    return render(request, 'wedding/gift_detail.html', {'gift' : gift})
