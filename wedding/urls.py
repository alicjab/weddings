from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gift_list, name='gift_list'),
]
