from django.http import JsonResponse

def hello(request):
    return JsonResponse({'message': 'Hello, World! this is V2'})
