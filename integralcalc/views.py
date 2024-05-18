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
            # retrieve user choice
            normal_without = request.POST.get('normalwithout')
            normal_input = request.POST.get('normal')
            between = request.POST.get('between')
            integral_border = request.POST.get('ingegralborder')
            c_input = request.POST.get('c')

            # evaluate user choice
            if normal_without == 'on':
                return render(request, 'integralcalc/partials/normal-without-input.html')
            elif normal_input == 'on':
                return render(request, 'integralcalc/partials/normal-input.html')
            elif between == 'on':
                return render(request, 'integralcalc/partials/between-input.html')
            elif integral_border == 'on':
                return render(request, 'integralcalc/partials/interval-border-input.html')
            elif c_input == 'on':
                return render(request, 'integralcalc/partials/c-input.html')
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, "integralcalc/partials/result.html", context)


class NormalWithout(View):
    def post(self, request, *args, **kwargs):
        try:
            input_data = request.POST.get('function')
            function = parse_expr(input_data.replace('^', '**'))
            area = normal(function)
            context = {'area': area}
            print(area)
            return render(request, 'integralcalc/partials/normal-without-result.html', context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, "integralcalc/partials/normal-without-result.html", context)


class Normal(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'integralcalc/partials/normal-result.html')


class Between(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'integralcalc/partials/between-result.html')


class Border(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'integralcalc/partials/interval-border-result.html')


class C(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'integralcalc/partials/c-result.html')
