from rest_framework import routers
from .views import SearchTaskViewSet


router = routers.DefaultRouter()
router.register(r'searchtask', SearchTaskViewSet)
urlpatterns = router.urls