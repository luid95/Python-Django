from django.conf.urls import url
from first_app import views


urlpatterns = [
    path('index/', views.index, name='index'),
]
