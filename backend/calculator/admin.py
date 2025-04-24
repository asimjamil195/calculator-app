from django.contrib import admin
from .models import CalculatorModel  # Assuming you have a model for calculations

# Register your models here.
admin.site.register(CalculatorModel)  # Register the model with the admin site