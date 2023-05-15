from django import forms
from .models import *

class SearchForm(forms.Form):
    ROOM_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'triple'),
        ('suite', 'Suite'),
    )
    
    destination = forms.ModelChoiceField(queryset=Destination.objects.all())
    typeOfRoom = forms.ChoiceField(choices = ROOM_CHOICES)
    num_nights = forms.IntegerField()
    budget = forms.IntegerField()
    
    
   
    

class FilterForm(forms.Form):
    offer= forms.BooleanField(required=False,initial=False)
    rate = forms.IntegerField(required=False,max_value=10,min_value=0)
    stars = forms.IntegerField(required=False,min_value=1,max_value=5)

class SortForm(forms.Form):
    sort = (
        ('highest_rating', 'highest_rating'),
        ('lowest_rating', 'lowest_rating'),
        ('lowest_stars', 'lowest_stars'),
        ('highest_stars', 'highest_stars'),
        ('highest_price','highest_price'),
        ('lowest_price','lowest_price')
    )
    sort_by = forms.ChoiceField(choices = sort)


   

   