from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Board app
    url(r'^', include('apps.board.urls', namespace='board')),
    # API
    url(r'^api/token/', obtain_auth_token, name='api-token'),
]
