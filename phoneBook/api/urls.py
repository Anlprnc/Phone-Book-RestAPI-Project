from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('phones', views.PhoneViewSet, basename='phone')

urlpatterns = router.urls
