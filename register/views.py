from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import SignUpForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.terms_confirmed =  form.cleaned_data.get('terms_confirmed')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request,'register/register.html',{'form':form})
