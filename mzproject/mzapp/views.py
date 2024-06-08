from django.shortcuts import render

# Create your views here.

def input_name(request):
    return render(request, 'main_page.html')

def main_page(request):
    return render(request,'main_page.html')