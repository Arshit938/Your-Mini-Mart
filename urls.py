"""ymm URL Configuration

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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('',views.index,name="index_main"),
    path('contact/',views.contact,name="contact us"),
    path('help/',views.help,name="help"),
    path('about/',views.about,name="about"),
    path('signin/',views.signin,name="signin"),
    path('search_prod/',views.search,name="search"),
    path('view_prod/',views.vp,name="search"),
    path('del_prod/',views.del_prod,name="dp"),
    path('cart/',views.Cart,name="crt"),
    path('signup/',views.signup,name='su'),
    path('add_to_cart/',views.addToCart,name="atc"),
    path('view_prod/shop/view_product/',views.vp,name='view2'),
    path('shop/view_product/',views.vp,name='view2'),
    path('view_prod/shop/addtocart/',views.addToCart,name='view2'),
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
