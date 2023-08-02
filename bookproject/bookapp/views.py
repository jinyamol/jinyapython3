from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import book
from.forms import BookForm


def index(request):
    Book=book.objects.all()
    context={
        'book_list':Book
    }
    return render(request,"index.html",context)
def details(request,book_id):
    Book=book.objects.get(id=book_id)
    return render(request,"details.html",{'book':Book})
def add_book(request):
    if request.method=="POST":
        name= request.POST.get('name',)
        desc = request.POST.get('desc', )
        price = request.POST.get('price', )
        img = request.FILES['img']
        Book= book(name=name,desc=desc,price=price,img=img)
        Book.save()
        return redirect('/')
    return render(request,"add.html")
def update(request,id):
    Book=book.objects.get(id=id)
    form=BookForm(request.POST or None,request.FILES,instance=Book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'book':Book})
def delete(request,id):
    if request.method=="POST":
        Book=book.objects.get(id=id)
        Book.delete()
        return redirect('/')
    return render(request,'delete.html')