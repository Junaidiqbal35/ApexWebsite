# Generated by Django 4.1.5 on 2023-01-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_mainheading', models.CharField(max_length=255, verbose_name='Banner Main Heading')),
                ('header_subheading', models.CharField(max_length=255, verbose_name='Banner Sub Heading')),
                ('header_caption', models.CharField(max_length=500, verbose_name='Header Caption')),
                ('welcome_text', models.TextField(verbose_name='Welcome Box Text')),
            ],
        ),
        migrations.CreateModel(
            name='LandlordPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_apex_rents_text', models.TextField(verbose_name='Why_Apex_Rents_Text')),
                ('lettings_text', models.TextField(verbose_name='Letting Text')),
                ('how_do_we_do_it_text', models.TextField(verbose_name='How Do We Do It Text')),
                ('trust_on_us_text', models.TextField(verbose_name='Trust On Us Text')),
            ],
        ),
        migrations.CreateModel(
            name='SellerPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_page_text', models.TextField(verbose_name='Seller Page')),
            ],
        ),
        migrations.CreateModel(
            name='TenantPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taking_care_of_you_text', models.TextField(verbose_name='Taking Care Of You Text')),
                ('peace_of_mind_text', models.TextField(verbose_name='Peace of Mind text')),
            ],
        ),
    ]
