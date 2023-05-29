from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('shop/view_product/', views.view_product,name='view'),
    path('/shop/view_product/',views.view_product,name='view2'),
    path('shop/search_prod/', views.search_product,name='search'),
    path('/shop/addtocart/', views.addToCart,name='atc'),
    path('cart/', views.Cart,name='cart'),
    path('help/',views.help,name="help"),
    path('signup/',views.signup,name='su'),
    path('shop/explore/',views.Explore,name="exp"),
    
] 