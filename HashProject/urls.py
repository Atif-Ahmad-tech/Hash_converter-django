from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
    re_path(r'^froala_editor/', include('froala_editor.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)