from django.conf.urls import url, handler404
# from django.conf.urls import handler404

from . import views

handler404 = views.error404

urlpatterns = [
    url(r'^$', views.gift_list, name='gift_list'),
    url(r'^gift/(?P<id>[0-9]+)/$', views.gift_detail, name='gift_detail'),
    url(r'^gift/new/$', views.gift_new, name='gift_new'),
    url(r'^gift/(?P<id>[0-9]+)/edit/$', views.gift_edit, name='gift_edit'),
    url(r'^gift/(?P<id>[0-9]+)/delete/$', views.gift_delete, name='gift_delete'),
]

