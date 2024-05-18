from django.urls import path
from integralcalc.views import IntegralCalc

urlpatterns = [
    path("integral", IntegralCalc.as_view(), name="integral")
]
