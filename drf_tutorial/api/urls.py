from rest_framework import routers
from drf_tutorial.api.viewsets import RecipeViewSet


router = routers.SimpleRouter()
router.register(r"recipes", RecipeViewSet)

urlpatterns = router.urls
