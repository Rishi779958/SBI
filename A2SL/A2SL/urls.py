"""A2SL URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# It defines URL patterns that map incoming web requests to specific views in our application.
from django.contrib import admin
from django.urls import path  # Provides functions for working with URLs.
from . import views  # handle incoming requests (views).

urlpatterns = [ # path = match incoming requests , views = that should be called when the URL pattern is matched. 
    path('admin/', admin.site.urls),
    path('about/',views.about_view,name='about'),  # When a user visits /about/, the about_view function is called to display the "About Us" page.
    path('contact/',views.contact_view,name='contact'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('animation/',views.animation_view,name='animation'),
    path('',views.home_view,name='home'),
    path('animation/',views.animation_view,name='animation')
]