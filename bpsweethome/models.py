from django.db import models
from django import forms
import yahoo.yql as yql

class SearchForm(forms.Form):
        """
                This class represents and validates the search form
        """
        location = forms.CharField()
        max_price = forms.IntegerField()
        min_beds = forms.IntegerField()

def searchProperties(form):
        """
                Receives a validated form and perform the nestoria
                search.
        """
        #Get the data from the input and build the YQL expression
        data = form.cleaned_data
        yqlQuery = """SELECT * FROM nestoria.search WHERE place_name='%s' and price_max='%s' and bedroom_min='%s' and has_photo='1' and listing_type='rent'""" % (data['location'], data['max_price'], data['min_beds'])

        response = yql.YQLQuery().execute(yqlQuery)

        results = list()

        #Check YQL response
        if 'query' in response and 'results' in response['query'] and response['query']['results'] and 'listings' in response['query']['results']:
                results = response['query']['results']['listings']

        return results
