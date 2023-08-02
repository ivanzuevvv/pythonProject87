from django.urls import path
from back.views import *


urlpatterns = [

    path('analiz/', prediction_view2, name='analiz'),
    path('', prediction_view, name=''),


]

