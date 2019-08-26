from rest_framework import routers
from .views import SearchTaskViewSet, CoOccurrenceViewSet


router = routers.DefaultRouter()
router.register(r'searchtask', SearchTaskViewSet)
router.register(r'cooccurrence', CoOccurrenceViewSet)
urlpatterns = router.urls
