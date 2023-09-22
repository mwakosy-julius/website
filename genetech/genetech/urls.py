from django.views.static import serve
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]