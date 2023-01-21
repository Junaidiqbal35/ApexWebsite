from django.contrib import admin
from .models import LandingPage, LandlordPage, TenantPage, SellerPage
# Register your models here.
admin.site.register(LandingPage)
admin.site.register(LandlordPage)
admin.site.register(TenantPage)
admin.site.register(SellerPage)