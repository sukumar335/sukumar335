from django.urls import path
from .views import home_view, extract_view, result_view

app_name = "app"

urlpatterns = [
    path('', home_view, name="home-view"),
    path('extract/', extract_view, name="extract-view"),
    path('result/<str:value>/<str:accuracy>/', result_view, name="result-view"),
]