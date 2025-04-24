from django.http import JsonResponse
from django.views import View

class CalculatorView(View):
    def get(self, request, operation):
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return JsonResponse({"error": "Division by zero is not allowed."}, status=400)
            result = a / b
        else:
            return JsonResponse({"error": "Invalid operation."}, status=400)

        return JsonResponse({"result": result})