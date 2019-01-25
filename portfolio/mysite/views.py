from django.shortcuts import render
from . models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=='POST':
        emailr=request.POST.get('email')
        subjectr=request.POST.get('subject')
        messager=request.POST.get('message')
        c=Contact(Email=emailr,Subject=subjectr,message=messager)
        c.save()
        return render(request,'thanks.html')
    else:
        return render(request,'contact.html')
def project(request):
    return render(request,'projects.html')
def about(request):
    return render(request,'about.html')
