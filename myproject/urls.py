"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('grammertool/', views.grammertool, name='grammertool'),
    path('translationtool/', views.translationtool, name='translationtool'),
    path('rephrasetool/', views.rephrasetool, name='rephrasetool'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path("grammar/fix/", views.grammar_fix, name="grammar_fix"),
    path("translate/fix/", views.translate_fix, name="translate_fix"),
    path('rephraser/', views.rephraser, name='rephraser'),
]