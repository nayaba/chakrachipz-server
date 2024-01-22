from django.shortcuts import render
from django.contrib.auth import logout
from allauth.account.views import SignupView, LoginView
from .models import Product

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cupcakes_index(request):
  cupcakes = Product.objects.all()
  return render(request, 'cupcakes.html', {
    'cupcakes': cupcakes
  })

def logout_view(request):
  logout(request)
  return redirect('/')

# class MySignupView(SignupView):
#     template_name = 'my_signup.html'


# class MyLoginView(LoginView):
#     template_name = 'account/google/login'