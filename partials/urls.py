from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('counter/<str:type>', views.counter, name='counter'),
]
