from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import menu,UserComments
from .forms import bookingForm,CommentForm
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

def form_view(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():  # if the users entered form data is in a valid format
            cd = form.cleaned_data
            uc = UserComments(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                comments=cd['comments'],  # Corrected to 'comments'
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blog.html', {'form': form})  