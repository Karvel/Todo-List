from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>[0-9]+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/(?P<pk>[0-9]+)/remove/$', views.item_remove, name='item_remove'),
]