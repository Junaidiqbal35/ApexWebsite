from django.db import models


# Create your models here.
class LandingPage(models.Model):
    header_mainheading = models.CharField(verbose_name='Banner Main Heading', max_length=255)
    header_subheading = models.CharField(verbose_name='Banner Sub Heading', max_length=255)
    header_caption = models.CharField(verbose_name='Header Caption', max_length=500)
    welcome_text = models.TextField(verbose_name='Welcome Box Text')

    def __str__(self):
        return self.header_subheading


class LandlordPage(models.Model):
    why_apex_rents_text = models.TextField(verbose_name='Why_Apex_Rents_Text')
    lettings_text = models.TextField(verbose_name='Letting Text')
    how_do_we_do_it_text = models.TextField(verbose_name='How Do We Do It Text')
    landlord_checklist = models.TextField(verbose_name='LandLord CheckList')
    trust_on_us_text = models.TextField(verbose_name='Trust On Us Text')

    # def __str__(self):
    #     return self.why_apex_rents_text


class TenantPage(models.Model):
    taking_care_of_you_text = models.TextField(verbose_name='Taking Care Of You Text')
    peace_of_mind_text = models.TextField(verbose_name='Peace of Mind text')


class SellerPage(models.Model):
    seller_page_text = models.TextField(verbose_name='Seller Page')


class InvestorPage(models.Model):
    investor_page_text = models.TextField(verbose_name='Investor Page')
