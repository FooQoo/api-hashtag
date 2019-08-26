from django.conf.urls import url, include
from django.contrib import admin
from hashtags.urls import router as my_router
from rest_framework_jwt.views import obtain_jwt_token
from hashtags.views import SearchTaskFilterViewSet


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token, name="jwt"),
    url(r'^api/v1/', include(my_router.urls)),
    url(r'^api/v1/task/(?P<hashtag>\w+)/$', SearchTaskFilterViewSet.as_view()),
]
