from django import forms 
from jadmin.models import Category

class DisplayFilterForm (forms.Form):
    player1_name= forms.CharField(
         max_length=30, required=True, label="Player Name", widget=forms.TextInput(attrs={'placeholder': 'Player Name...'}) )
    player2_name= forms.CharField(
         max_length=30, required=True, label="Player Name", widget=forms.TextInput(attrs={'placeholder': 'Player Name...'}) )
    player3_name= forms.CharField(
         max_length=30, required=True, label="Player Name", widget=forms.TextInput(attrs={'placeholder': 'Player Name...'}) )
   
   
    cat1 = forms.ModelChoiceField( 
        queryset=Category.objects.all(), empty_label="-- Select an Option --", label="Choose Category 1" )
    cat2 = forms.ModelChoiceField( 
        queryset=Category.objects.all(), empty_label="-- Select an Option --", label="Choose Category 2" )
    cat3 = forms.ModelChoiceField( 
        queryset=Category.objects.all(), empty_label="-- Select an Option --", label="Choose Category 3" )
    cat4 = forms.ModelChoiceField( 
        queryset=Category.objects.all(), empty_label="-- Select an Option --", label="Choose Category 4" )
    cat5 = forms.ModelChoiceField( 
        queryset=Category.objects.all(), empty_label="-- Select an Option --", label="Choose Category 5" )
    cat6 = forms.ModelChoiceField( 
        queryset=Category.objects.all(), empty_label="-- Select an Option --", label="Choose Category 6" )
    
    