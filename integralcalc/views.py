from django.shortcuts import render
from django.views import View
from sympy.parsing.sympy_parser import parse_expr
from integralcalc.integral import normal


# Create your views here.

class IntegralCalc(View):
    def get(self, request, *args, **kwargs):
        return render(request, "integralcalc/home.html")

    def post(self, request, *args, **kwargs):
        try:
            input_data = request.POST.get('function')
            function = parse_expr(input_data.replace('^', '**'))
            area = normal(function)
            context = {'area': area}
            print(area)
            return render(request, "integralcalc/partials/result.html", context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, "integralcalc/partials/result.html", context)
