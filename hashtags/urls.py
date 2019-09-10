from rest_framework import routers
from .views import CoOccurrenceViewSet, BitermViewSet


router = routers.DefaultRouter()
router.register(r'cooccurrence', CoOccurrenceViewSet)
router.register(r'biterm', BitermViewSet)
urlpatterns = router.urls
