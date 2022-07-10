from multiprocessing import context
# from tkinter.tix import Select
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
def index(request):
      return render(request, 'index.html')
      # return HttpResponse("this is a homepage")
def about(request):
      return render(request, 'about.html')
      
def services(request):
      return render(request, 'services.html')
def contact(request):
      if request.method == "POST":
            Name = request.POST.get('name')
            Email = request.POST.get('Email')
            Number = request.POST.get('Number')
            select = request.POST.get('select')
            contact = Contact(Name = Name,Email = Email, Number = Number, select = select, date = datetime.today())
            contact.save()
      return render(request, 'contact.html')
      