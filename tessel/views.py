from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    username = "Name not entered"
   
    if request.method == "POST":
      #Get the posted form
      MyLoginForm = NameForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
    else:
      MyLoginForm = NameForm()
		
    return render(request, 'index.html', {"username" : username})

def home(request):
    return render(request,'name.html')
