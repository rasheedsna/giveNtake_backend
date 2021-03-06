from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet)
router.register(r'state', StateViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'block', BlockViewSet)
router.register(r'panchayath', PanchayathViewSet)
router.register(r'ward', WardViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name="user_login"),
    
    ]