"""project_hope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app_hope.views import Inicio, Login, Logout, Conta, Cadastro
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view(), name="inicio"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('cadastro', Cadastro.as_view(), name="cadastro"),
    path('conta', Conta.as_view(), name="conta"),
    path('accounts/login/?next=/conta', Conta.as_view(), name="conta"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app_hope/password/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="app_hope/password/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="app_hope/password/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app_hope/password/password_reset_complete.html"), name="password_reset_complete"),
]
