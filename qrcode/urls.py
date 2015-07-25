from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quest', views.quest, name='quest'),
    # url(r'^encode/(?P<encode_text>[0-9a-zA-Z]+)/$', views.encode, name='encode'),
    url(r'^encode/$', views.encode, name='encode'),
]