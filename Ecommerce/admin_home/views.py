from django.shortcuts import render

# Create your views here.
def admin_home_index(request):
    return render(request,'admin_home/homepage.html')
def add(request):
    return render(request,'admin_home/addProduct.html')
def delete(request):
    return render(request,'admin_home/deleteProduct.html')
def update(request):
    return render(request,'admin_home/updateProduct.html')
