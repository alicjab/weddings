#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect

from .forms import GiftForm
from .models import Gift

def gift_list(request):
    new_gifts = Gift.objects.filter(accepted=False)
    accepted_gifts = Gift.objects.filter(accepted=True)
    # 'user' : request.user, 
    return render(request, 'wedding/gift_list.html', {'new_gifts' : new_gifts, 'accepted_gifts' : accepted_gifts})

def gift_detail(request, id):
    gift = get_object_or_404(Gift, id=id)
    return render(request, 'wedding/gift_detail.html', {'gift' : gift})

def gift_new(request):
    if request.method == "POST":
        form = GiftForm(request.POST)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.proposed_by = request.user
            if request.user.is_superuser:
                gift.accepted = True
            gift.save()
            return redirect('gift_detail', id=gift.id)
    else:
        form = GiftForm()
    return render(request, 'wedding/gift_edit.html', {'form': form})

def gift_edit(request, id):
    gift = get_object_or_404(Gift, id=id)
    if request.method == "POST":
        form = GiftForm(request.POST, instance=gift)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.proposed_by = request.user
            gift.save()
            return redirect('gift_detail', id=gift.id)
    else:
        form = GiftForm(instance=gift)
    return render(request, 'wedding/gift_edit.html', {'form': form})


def gift_delete(request, id):
    gift = get_object_or_404(Gift, id=id)
    Gift.objects.filter(id=id).delete()
    # Trzeba bedzie dodac info ze udalo sie usunac
    new_gifts = Gift.objects.filter(accepted=False)
    accepted_gifts = Gift.objects.filter(accepted=True)
    return render(request, 'wedding/gift_list.html', {'new_gifts' : new_gifts, 'accepted_gifts' : accepted_gifts})


def error404(request):
    return render(request, 'wedding/404.html')

