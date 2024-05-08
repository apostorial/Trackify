from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("MemberInfo:stats")
        else:
            messages.success(request, ("There was an error logging in, please try again."))
            return redirect("Member:login")
    else:
        return render(request, 'member/login.html', {})
    
def logoutUser(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect("Member:login")

def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful."))
            return redirect("MemberInfo:addInfo")
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }

    return render(request, 'member/register.html', context)