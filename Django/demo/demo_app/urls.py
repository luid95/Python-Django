from django.conf.urls import url
from demo_app import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
