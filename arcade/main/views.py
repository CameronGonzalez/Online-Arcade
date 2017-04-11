from django.shortcuts import render

def index(request):
   return render(request, 'main/index.html')

def snake(request):
   return render(request, 'main/snake.html')

def pong(request):
   return render(request, 'main/pong.html')

def spaceInvaders(request):
   return render(request, 'main/spaceInvaders.html')

def tetris(request):
   return render(request, 'main/tetris.html')

def pacMan(request):
   return render(request, 'main/pacMan.html')

def brickBreaker(request):
   return render(request, 'main/brickBreaker.html')

def avalanche(request):
   return render(request, 'main/avalanche.html')

def fishy(request):
   return render(request, 'main/fishy.html')

def mimelet(request):
   return render(request, 'main/mimelet.html')

def pyro(request):
   return render(request, 'main/pyro.html')

def agario(request):
   return render(request, 'main/agario.html')

def splixio(request):
   return render(request, 'main/splixio.html')

# Create your views here.
