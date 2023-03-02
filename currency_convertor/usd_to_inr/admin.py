from django.contrib import admin
from . models import GDP_IN_US_dollar

# Register your models here.

@admin.register(GDP_IN_US_dollar)
class GDP_IN_US_dollorAdmin(admin.ModelAdmin):
    list_display =['id','year','gdp_usd']