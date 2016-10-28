#-*- coding: utf-8 -*-

from django.shortcuts import render

def gift_list(request):
    return render(request, 'wedding/gift_list.html', {})
