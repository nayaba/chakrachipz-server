from django.shortcuts import render

cupcakes = ['lemon rose', 'vanilla chai', 'chocolate chip cookie dough']

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cupcakes_index(request):
  return render(request, 'cupcakes.html', {
    'cupcakes': cupcakes
  })