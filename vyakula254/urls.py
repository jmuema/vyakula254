from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('resturants.urls')),
    url('accounts/', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
