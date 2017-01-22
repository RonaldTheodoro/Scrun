from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Board app
    url(r'^', include('apps.board.urls', namespace='board')),
]
