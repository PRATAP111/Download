from django.shortcuts import render

def home(request):
    name = "<h1> PRATAP </h1> "
    return render(request,'index.html',{'name':name})