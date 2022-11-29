from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    return render(request,"authentication/signup.html")

def handlelogin(request):
    return render(request,"authentication/login.html")


def handlelogout(request):
    return redirect('/authcart/login')