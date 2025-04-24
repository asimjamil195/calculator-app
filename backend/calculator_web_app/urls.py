from django.urls import path
from calculator.views import CalculatorView

urlpatterns = [
    path('calculate/', CalculatorView.as_view(), name='calculate'),
]