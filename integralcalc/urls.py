from django.urls import path
from integralcalc.views import IntegralCalc, NormalWithout, Normal, Between, Border, C

urlpatterns = [
    path("integral", IntegralCalc.as_view(), name="integral"),
    path('integral/normal-without', NormalWithout.as_view(), name='normal-without'),
    path('integral/normal', Normal.as_view(), name='normal'),
    path('integral/between', Between.as_view(), name='between'),
    path('integral/border', Border.as_view(), name='border'),
    path('integral/c', C.as_view(), name='c')
]
