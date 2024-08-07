from django.shortcuts import render
from . forms import UserForm
from django.http import HttpResponse
from . models import Login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST,request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             file = form.cleaned_data['file']
#             user = Login(name=name,last_name=last_name,email=email,file=file)
#             user.save()
           
#             return HttpResponse ('success')
#     else:
#             form = LoginForm()
 
#     return render(request,'loginform.html',{'form':form})

# def success_view(request):
#     return HttpResponse('form submission succesful')
@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submitted successfully')
    else:
        form = UserForm()

    return render(request,'loginform.html',{'form':form})