from django.contrib.auth import views as auth_views
from django.urls import path 
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home',),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='conv_csv/signin.html',
        authentication_form = LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view()
         , {'next_page': '/core'}, name='logout'),
    path('convert/', views.csv_to_shapefile, name='convert'),
    path('shpF/', views.csv_to_shapefile, name='shap'),
    
]