from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.ProfileViewset,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)


urlpatterns = [
    path('profiles/', views.ProfilesApiview.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))

]