from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include("menu.urls")),
    path('restaurants/', include("restaurants.urls")),
    path('accounts/', include("accounts.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # static은 list를 반환
