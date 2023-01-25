
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
