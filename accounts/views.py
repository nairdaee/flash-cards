from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout #function for loging in/out the user


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #saving user
            login(request, user) 
            
            return redirect("home")
    else:

        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form': form})
