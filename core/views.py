from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.forms import TenantContactForm, LandLordContactForm, SellerContactForm, InvestmentContactForm, \
    ProjectQuoteForm
# Create your views here.
from core.models import LandingPage, LandlordPage, TenantPage, SellerPage, InvestorPage


def landing_page(request):
    landing_data = LandingPage.objects.first()
    context = {'landing_data': landing_data}
    return render(request, 'landing-page.html', context)


class LandLordFormView(FormView):
    template_name = 'landlord.html'
    form_class = LandLordContactForm
    success_url = reverse_lazy('landlord')

    def get_context_data(self, **kwargs):
        context = super(LandLordFormView, self).get_context_data(**kwargs)
        land_load_data = LandlordPage.objects.first()
        context['land_lord_data'] = land_load_data
        return context

    def form_valid(self, form):
        # Send email using the form's cleaned data
        # (You should have EMAIL settings configured in settings.py)
        message = f"Full Name: {form.cleaned_data['full_name']}\n"
        message += f"Email: {form.cleaned_data['email']}\n"
        message += f"Phone Number: {form.cleaned_data['phone_number']}\n"
        message += f"Monthly Rent: {form.cleaned_data['monthly_rent']}\n"
        message += f"Address: {form.cleaned_data['address']}\n"
        message += f"Property Type: {form.cleaned_data['property_type']}\n"
        message += f"Beds: {form.cleaned_data['bedrooms']}\n"
        message += f"Comments: {form.cleaned_data['comment']}"

        send_mail(
            'New LandLord Inquiry',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.RECIPIENT_EMAIL],
        )
        messages.success(self.request, "Thank you for your submission, we will be in touch soon!")
        return super().form_valid(form)



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
        message += f"Property Type: {form.cleaned_data['property_type']}\n"
        message += f"Beds: {form.cleaned_data['bedrooms']}\n"
        message += f"Comments: {form.cleaned_data['comment']}"

        send_mail(
            'New Tenant Inquiry',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['junaidiqbal0323@gmail.com', settings.RECIPIENT_EMAIL],
        )
        messages.success(self.request, "Thank you for your submission, we will be in touch soon!")
        return super().form_valid(form)
class SellerContactFormView(FormView):
    template_name = 'seller.html'
    form_class = SellerContactForm
    success_url = reverse_lazy('seller')

    def get_context_data(self, **kwargs):
        context = super(SellerContactFormView, self).get_context_data(**kwargs)
        seller_data = SellerPage.objects.first()
        context['seller_data'] = seller_data
        return context

    def form_valid(self, form):
        # Send email using the form's cleaned data
        # (You should have EMAIL settings configured in settings.py)
        message = f"Full Name: {form.cleaned_data['full_name']}\n"
        message += f"Email: {form.cleaned_data['email']}\n"
        message += f"Phone Number: {form.cleaned_data['phone_number']}\n"
        message += f"Address: {form.cleaned_data['address']}\n"
        message += f"City: {form.cleaned_data['city']}\n"
        message += f"Property Type: {form.cleaned_data['property_type']}\n"
        message += f"Beds: {form.cleaned_data['bedrooms']}\n"
        message += f"Comments: {form.cleaned_data['comment']}"

        send_mail(
            'New Seller Inquiry',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.RECIPIENT_EMAIL],
        )
        messages.success(self.request, "Thank you for your submission, we will be in touch soon!")
        return super().form_valid(form)








class InvestorContactFormView(FormView):
    template_name = 'investors.html'
    form_class = InvestmentContactForm
    success_url = reverse_lazy('investors')

    def get_context_data(self, **kwargs):
        context = super(InvestorContactFormView, self).get_context_data(**kwargs)
        investor_data = InvestorPage.objects.first()
        context['investor_data'] = investor_data
        return context

    def form_valid(self, form):
        # Send email using the form's cleaned data
        # (You should have EMAIL settings configured in settings.py)
        message = f"Full Name: {form.cleaned_data['full_name']}\n"
        message += f"Email: {form.cleaned_data['email']}\n"
        message += f"Phone Number: {form.cleaned_data['phone_number']}\n"
        message += f"Address: {form.cleaned_data['address']}\n"
        message += f"City: {form.cleaned_data['city']}\n"
        message += f"Property Type: {form.cleaned_data['property_type']}\n"
        message += f"Comments: {form.cleaned_data['comment']}"

        send_mail(
            'New Investor Inquiry',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.RECIPIENT_EMAIL],
        )
        messages.success(self.request, "Thank you for your submission, we will be in touch soon!")
        return super().form_valid(form)



class ProjectQuoteFormView(FormView):
    template_name = 'project_quote_page.html'
    form_class = ProjectQuoteForm
    success_url = reverse_lazy('project_quote')

    def get_context_data(self, **kwargs):
        context = super(ProjectQuoteFormView, self).get_context_data(**kwargs)
        # Add any additional context if needed
        return context

    def form_valid(self, form):
        # Send email using the form's cleaned data
        message = f"Full Name: {form.cleaned_data['full_name']}\n"
        message += f"Email Address: {form.cleaned_data['email_address']}\n"
        message += f"Phone Number: {form.cleaned_data['phone_number']}\n"
        message += f"Project Type: {form.cleaned_data['project_type']}\n"
        message += f"Project Description: {form.cleaned_data['project_description']}\n"
        message += f"Requested Loan Amount: {form.cleaned_data['requested_loan_amount']}\n"
        message += f"Estimated Project Value Upon Completion: {form.cleaned_data['estimated_project_value_upon_completion']}\n"
        message += f"Own Equity Contribution: {form.cleaned_data['own_equity_contribution']}\n"
        message += f"Estimated Credit Score: {form.cleaned_data['estimated_credit_score']}\n"
        message += f"Additional Information: {form.cleaned_data['additional_information']}"

        send_mail(
            'New Project Inquiry',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.RECIPIENT_EMAIL],
        )
        messages.success(self.request, "Thank you for your submission, we will be in touch soon!")
        return super().form_valid(form)