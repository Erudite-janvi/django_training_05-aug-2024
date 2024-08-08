from django.shortcuts import render,redirect
from django.http import HttpResponse

# def demo(request):
#     return HttpResponse('Hello World from Django Sessions!')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == username and password == password:
            request.session['username']= username
            print("Session is Created:",request.session.get('username'))
            return redirect('home')
        else:
            return render(request,'session/login.html',{'error':'Invalid Credentials'})

    return render(request,'session/login.html')    

def logout_view(request):
    request.session.flush()
    return redirect('login')

def home_view(request):
    username = request.session.get('username','Guest')
    return render(request,'session/home.html',{'username':username})