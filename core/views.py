from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.forms import TenantContactForm
# Create your views here.
from core.models import LandingPage, LandlordPage, TenantPage, SellerPage, InvestorPage


def landing_page(request):
    landing_data = LandingPage.objects.first()
    context = {'landing_data': landing_data}
    return render(request, 'landing-page.html', context)


def landlord_page(request):
    land_load_data = LandlordPage.objects.first()
    context = {'land_lord_data': land_load_data}
    return render(request, 'landlord.html', context)


# def tenant_page(request):
#     tenant_data = TenantPage.objects.first()
#     context = {'tenant_data': tenant_data}
#     return render(request, 'tenants.html', context)


class TenantContactFormView(FormView):
    template_name = 'tenants.html'
    form_class = TenantContactForm
    success_url = reverse_lazy('tenants')

    def get_context_data(self, **kwargs):
        context = super(TenantContactFormView, self).get_context_data(**kwargs)
        context['tenant_data'] = TenantPage.objects.first()
        return context

    def form_valid(self, form):
        # Send email using the form's cleaned data
        # (You should have EMAIL settings configured in settings.py)
        message = f"Full Name: {form.cleaned_data['full_name']}\n"
        message += f"Email: {form.cleaned_data['email']}\n"
        message += f"Phone Number: {form.cleaned_data['phone_number']}\n"
        message += f"Monthly Budget: {form.cleaned_data['monthly_budget']}\n"
        message += f"Location of Interest: {form.cleaned_data['location_of_interest']}\n"
        message += f"Beds: {form.cleaned_data['bedrooms']}\n"
        message += f"Comments: {form.cleaned_data['comment']}"

        send_mail(
            'New Tenant Inquiry',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['junaidiqbal0323@gmail.com'],
        )
        return super().form_valid(form)





def seller_page(request):
    seller_data = SellerPage.objects.first()
    context = {'seller_data': seller_data}
    return render(request, 'seller.html', context)

def investor_page(request):
    investor_data = InvestorPage.objects.first()
    context = {'investor_data': investor_data}
    return render(request, 'investors.html', context)
