from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gift_list, name='gift_list'),
    url(r'^gift/(?P<id>[0-9]+)/$', views.gift_detail, name='gift_detail'),
    url(r'^gift/new/$', views.gift_new, name='gift_new'),
    url(r'^gift/(?P<id>[0-9]+)/edit/$', views.gift_edit, name='gift_edit'),


    

]
