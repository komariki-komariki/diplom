from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from app import views
from app.views import BasketView, OrderView, PartnerUpdate, PartnerOrdersView

router = DefaultRouter()
router.register("shops", views.ShopView, basename='shops')
router.register("category", views.CategoryApiView, basename='category')
router.register("products", views.ProductApiView, basename='products')
router.register("product_info", views.ProductInfoView, basename='product_info')

urlpatterns = [
    path('', include(router.urls)),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('users/', views.users_view, name='users'),
    path('load/', PartnerUpdate.as_view(), name='partner-load'),
    path('part_order/', PartnerOrdersView.as_view(), name='partner-order'),
    path('user/basket', BasketView.as_view(), name='user-basket'),
    path('user/orders', OrderView.as_view(), name='user-orders'),
]
