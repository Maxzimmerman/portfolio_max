from django.urls import path
from .views import index

urlpatterns = [
    path("portfolio", index, name="portfolio"),
]
