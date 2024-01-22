from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cupcakes/', views.cupcakes_index, name='index'),
  path('logout/', views.logout_view),
  # path('login', views.account_login)
]