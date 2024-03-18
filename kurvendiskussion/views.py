from django.shortcuts import render
from django.views.generic import View
import re
from .calc import Calc
from sympy import symbols, simplify


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'kurvendiskussion/home.html')

    def post(self, request, *args, **kwargs):
        input_data = request.POST.get('input-field')
        function = simplify(input_data)
        calc = Calc(function)
        calc.gebe_exponenten_zurück(function)
        calc.bestimme_y_achsenabschnitt(function)
        calc.bestimme_symmetrie(calc.gebe_exponenten_zurück(function))
        calc.bestimme_grenzwertverhalten(-100, 100, function)
        calc.ermittle_ableitungen(function)
        calc.ermittle_nullstellen(function)
        calc.ermittle_extremstellen(calc.f1, function)
        calc.ermittle_wendestellen()
        calc.monotonie(-100, 100)
        calc.krümmung(-100, 100)
        context = {'calc': calc}
        return render(request, "kurvendiskussion/partials/result.html", context)
