from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'main/index.html')
# ('<h4>Hello, Aleksei</h4><p><a href="contact">Контактная информация</a></p>')
def about(request):
    return render(request,'main/about.html')
def contact(request):
    return HttpResponse('<h3>Контактная информация скоро здесь появится</h3>')
