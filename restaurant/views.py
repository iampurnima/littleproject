from django.shortcuts import render
from django.http import HttpResponse
from .models import menu
from .forms import bookingForm
# Create your views here.
def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')

def book(request):
    form = bookingForm()
    if request.method == 'post':
        form = bookingForm(request.post)
        if form.is_valid():
            form.save()
    context = {'form':form}        
    return render(request,'book.html',context)

def menuPage(request):
    menu_data = menu.objects.all()
    main_data = {"menu":menu_data}
    return render(request,'menu.html',{"menu":main_data})

def display_menu_item(request,pk=None):
    if pk:
        menu_item = menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request,'menu_item.html',{'menu_item':menu_item})