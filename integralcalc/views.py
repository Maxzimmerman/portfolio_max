from django.shortcuts import render
from django.views import View
from sympy.parsing.sympy_parser import parse_expr
from integralcalc.integral import normal, between, with_one_interval_border, calc_c


# Create your views here.

class IntegralCalc(View):
    def get(self, request, *args, **kwargs):
        return render(request, "integralcalc/home.html")

    def post(self, request, *args, **kwargs):
        try:
            # retrieve user choice
            normal_without = request.POST.get('normalwithout')
            normal_input = request.POST.get('normal')
            between_input = request.POST.get('between')
            integral_border = request.POST.get('ingegralborder')
            c_input = request.POST.get('c')

            # evaluate user choice
            if normal_without == 'on':
                return render(request, 'integralcalc/partials/normal-without-input.html')
            elif normal_input == 'on':
                return render(request, 'integralcalc/partials/normal-input.html')
            elif between_input == 'on':
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
            return render(request, 'integralcalc/partials/normal-without-result.html', context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, "integralcalc/partials/normal-without-result.html", context)


class Normal(View):
    def post(self, request, *args, **kwargs):
        try:
            # get the data
            function_data = request.POST.get('function')
            interval_data = request.POST.get('interval')
            # bring data in the correct shape
            interval = [int(x) for x in interval_data.split(';')]
            function = parse_expr(function_data.replace('^', '**'))
            # calculate the inputs
            area = normal(function, interval)
            context = {'area': area}
            return render(request, 'integralcalc/partials/normal-result.html', context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, "integralcalc/partials/normal-result.html", context)


class Between(View):
    def post(self, request, *args, **kwargs):
        try:
            # get user data
            function_data_one = request.POST.get('function')
            function_data_two = request.POST.get('second-function')
            # bring user data in correct shape
            function_one = parse_expr(function_data_one.replace('^', '**'))
            function_two = parse_expr(function_data_two.replace('^', '**'))
            # precess the input data
            area = between(function_one, function_two)
            context = {'area': area}
            print(area)
            return render(request, 'integralcalc/partials/between-result.html', context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, 'integralcalc/partials/between-result.html', context)


class Border(View):
    def post(self, request, *args, **kwargs):
        try:
            # get data
            function_data = request.POST.get('function')
            first_interval_border_data = request.POST.get('first-border')
            area_input_data = request.POST.get('area')
            # bring data in right shape
            function = parse_expr(function_data.replace('^', '**'))
            first_interval_border = int(first_interval_border_data)
            area_input = int(area_input_data)
            # process data
            result = with_one_interval_border(function, first_interval_border, area_input)
            context = {'result': result}
            return render(request, 'integralcalc/partials/interval-border-result.html', context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, 'integralcalc/partials/between-result.html', context)


class C(View):
    def post(self, request, *args, **kwargs):
        try:
            # get input data
            function_data = request.POST.get('function')
            point_data = request.POST.get('point')
            # bring input data in right form
            function = parse_expr(function_data.replace('^', '**'))
            point_modified = point_data.split(',')
            point = {int(point_modified[0]): int(point_modified[1])}
            # process input data
            result = calc_c(function, point)
            context = {'result': result}
            return render(request, 'integralcalc/partials/c-result.html', context)
        except:
            context = {'error': "Ups die Eingabe ist Fehlerhaft. Versuche es erneut."}
            return render(request, 'integralcalc/partials/c-result.html', context)
