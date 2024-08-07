from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# def demo(request):
#     return render(request,'home.html')
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe= False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.error,status=400)

@csrf_exempt
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:
        return JsonResponse({'error':'user not found'},status = 404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors,status= 400)
        
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse("successfulyy deleted",status= 204)
    else:
        return HttpResponse(status=405)