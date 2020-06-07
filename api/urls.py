from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('product-viewset',views.ProductsViewSet,base_name='product-viewset')


urlpatterns = [
    path('products/', views.ProductsApiview.as_view()),
    path('',include(router.urls))

]