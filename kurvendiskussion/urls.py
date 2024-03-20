from django.urls import path, include
from . import views

urlpatterns = [
    path('kurvendiskussion/', views.HomeView.as_view(), name='kurvendiskussion'),
    path('test', views.TestView.as_view())
]
