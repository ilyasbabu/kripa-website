from django.shortcuts import render
from .models import Gallery

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact-us.html')

def gallery(request):
    photo=Gallery.objects.all()
    context={
        'photo':photo
    }
    return render(request, 'gallery.html',context)