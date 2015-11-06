from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^item/(?P<pk>[0-9]+)/new_item/$', views.add_item_to_list, name='add_item_to_list'),
    url(r'^item/(?P<pk>[0-9]+)/remove/$', views.item_remove, name='item_remove'),
]