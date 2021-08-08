from django.urls import path
from django.views.generic import TemplateView

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('thanks/', TemplateView.as_view(template_name='accounts/thanks.html'), name='thanks'),
]