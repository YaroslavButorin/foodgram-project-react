from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import IngredientsViewSet, RecipeViewSet, TagsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)