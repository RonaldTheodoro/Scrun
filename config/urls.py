from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from apps.board.urls import router


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # API
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]
