from django.shortcuts import render
import pandas as pds
from . models import GDP_IN_US_dollar
import requests
# Create your views here.

def Graph(request):
    if request.method == 'POST':
        key = '179279559d22483bacb26e41147cb467'
        response = requests.get(f'https://api.currencyfreaks.com/latest?apikey={key}').json()
        rates = response['rates']
        INR = rates['INR']
        data =GDP_IN_US_dollar.objects.all().values()
        df = pds.DataFrame(data)
        year = df.year.tolist()
        gdp_usd = df.gdp_usd.tolist()
        gdp_inr= []
        for i in gdp_usd:
            gdp_inr.append(i*float(INR))
        mydict={
            'title': 'Indian GDP in INR billion',
            'year': year,
            'gdp' : gdp_inr
        }
        return render(request, 'index.html',context=mydict)
    else:
        data =GDP_IN_US_dollar.objects.all().values()
        df = pds.DataFrame(data)
        year = df.year.tolist()
        gdp_usd = df.gdp_usd.tolist()
        mydict={
            'year' : year,
            'gdp' : gdp_usd,
            'title': 'Indian GDP in USD billion'
        }
        return render(request, 'index.html', context=mydict)
