from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            return HttpResponse("password incorrect") 
            # return render(request,'auth/signup.html')                   
        try:
            if User.objects.get(username=email):
                return HttpResponse("email already exist")
                # return render(request,'auth/signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User created",email)
    return render(request,"signup.html")





def handlelogin(request):
    return render(request,"login.html")


def handlelogout(request):
    return redirect('/auth/login')