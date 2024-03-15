from django.shortcuts import render
from django.views.generic import View
import re


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'kurvendiskussion/home.html')

    def post(self, request, *args, **kwargs):
        input_data = request.POST.get('input-field')
        r = re.split("\+|-", input_data)
        print(r)
        print("hello")
        return render(request, "kurvendiskussion/partials/result.html")
