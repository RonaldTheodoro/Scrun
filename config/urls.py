from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from apps.board.urls import router


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Index
    url(r'^$', TemplateView.as_view(template_name='board/index.html')),
    # API
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]
