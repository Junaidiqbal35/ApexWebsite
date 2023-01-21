from django.shortcuts import render

# Create your views here.
from core.models import LandingPage, LandlordPage, TenantPage, SellerPage


def landing_page(request):
    landing_data = LandingPage.objects.first()
    context = {'landing_data': landing_data}
    return render(request, 'landing-page.html', context)


def landlord_page(request):
    land_load_data = LandlordPage.objects.first()
    context = {'land_lord_data': land_load_data}
    return render(request, 'landlord.html', context)


def tenant_page(request):
    tenant_data = TenantPage.objects.first()
    context = {'tenant_data': tenant_data}
    return render(request, 'tenants.html', context)


def seller_page(request):
    seller_data = SellerPage.objects.first()
    context = {'seller_data': seller_data}
    return render(request, 'seller.html', context)
