from django.shortcuts import render

def index(request):
    return render(request, "index.html") 

def about(request):
    return render(request, "about.html") 

def products(request):
    return render(request, "products.html") 

def blog(request):
    return render(request, "blog.html")

def gallery(request):
    return render(request, "gallery.html")

def contacts(request):
    return render(request, "contacts.html") 
