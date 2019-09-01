from rest_framework import routers
from .views import HashtagTaskViewSet, CoOccurrenceViewSet, BitermViewSet


router = routers.DefaultRouter()
router.register(r'hashtagtask', HashtagTaskViewSet)
router.register(r'cooccurrence', CoOccurrenceViewSet)
router.register(r'biterm', BitermViewSet)
urlpatterns = router.urls
