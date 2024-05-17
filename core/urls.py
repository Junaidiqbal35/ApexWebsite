from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing_page, name="home"),
    path('landlord/', views.LandLordFormView.as_view(), name="landlord"),
    path('seller/', views.SellerContactFormView.as_view(), name="seller"),
    path('tenants/', views.TenantContactFormView.as_view(), name="tenants"),
    path('investors/', views.InvestorContactFormView.as_view(), name="investors")
]