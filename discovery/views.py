from django.shortcuts import render, HttpResponse, redirect
from .forms import FormRegistration          
from .models import Customer        
from .models import Book 

# Create your views here.

def index(request):
    user_form = FormRegistration()           
    if request.method == 'POST':
        user_form = FormRegistration(request.POST)                         
        if user_form.is_valid():
            fname = user_form['name']   
            fsecond_name = user_form['second_name']
            femail = user_form['email']
            fpassword = user_form['password']

            creat_user=Customer.objects.create(name=fname, second_name=fsecond_name, email=femail, password=fpassword)            
            creat_user.save()        
            return redirect("catalog")  
        else:
            return HttpResponse(f"Форма не валидна")
    else:
        return render(request, 'Registration.html', {'key':user_form})    


def reg(request):
    return render(request, "not_registr.html")


def store_catalog(request):                 # КАТАЛОГ
    books = Book.objects.all()              
    return render(request, "catalog.html", {'bk': books})            


def product(request, book_id):                   #   ОДИН ПРОДУКТ
    book = Book.objects.get(id=book_id)              
    return render(request, "product.html", locals())  







'''
def book(request, book_id):
    get_book=Book.objects.get(id=book_id)

    return render(request,'book.html',{'get_book':get_book})          
'''
