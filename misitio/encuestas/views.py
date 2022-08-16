from django.shortcuts import render
from django.http import HttpResponse
from encuestas.models import Noticia


# Create your views here.
def index(request):
     noticia2 = Noticia.objects.all()  
     return render(request, 'index.html', {'noticia2': noticia2})
    
def principal(request):
     return render(request, 'principal.html')
     
def contactenos(request):
     return render(request, 'contacto.html')