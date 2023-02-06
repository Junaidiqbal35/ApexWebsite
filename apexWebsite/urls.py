from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import landing_page, landlord_page, tenant_page, seller_page,investor_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="home"),
    path('landlord/', landlord_page, name="landlord"),
    path('seller/', seller_page, name="seller"),
    path('tenants/', tenant_page, name="tenants"),
    path('investors/', investor_page, name="investors")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
