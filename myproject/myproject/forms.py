from django import forms 
from jadmin.models import Category

class DisplayFilterForm(forms.Form):
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
    
class NewCategoryForm(forms.Form):
        category_name= forms.CharField(
            max_length=50, required=True, label="Category Name", widget=forms.TextInput(attrs={'placeholder': 'Category Name...'}) )
        question_100 = forms.CharField(
            max_length=50, required=True, label="$100 Question", widget=forms.TextInput(attrs={'placeholder': 'Question...'}) )
        answer_100 = forms.CharField(
            max_length=50, required=True, label="$100 Answer", widget=forms.TextInput(attrs={'placeholder': 'Answer...'}) )
        question_200 = forms.CharField(
            max_length=50, required=True, label="$200 Question", widget=forms.TextInput(attrs={'placeholder': 'Question...'}) )
        answer_200 = forms.CharField(
            max_length=50, required=True, label="$200 Answer", widget=forms.TextInput(attrs={'placeholder': 'Answer...'}) )
        question_300 = forms.CharField(
            max_length=50, required=True, label="$300 Question", widget=forms.TextInput(attrs={'placeholder': 'Question...'}) )
        answer_300 = forms.CharField(
            max_length=50, required=True, label="$300 Answer", widget=forms.TextInput(attrs={'placeholder': 'Answer...'}) )
        question_400 = forms.CharField(
            max_length=50, required=True, label="$400 Question", widget=forms.TextInput(attrs={'placeholder': 'Question...'}) )
        answer_400 = forms.CharField(
            max_length=50, required=True, label="$400 Answer", widget=forms.TextInput(attrs={'placeholder': 'Answer...'}) )
        question_500 = forms.CharField(
            max_length=50, required=True, label="$500 Question", widget=forms.TextInput(attrs={'placeholder': 'Question...'}) )
        answer_500 = forms.CharField(
            max_length=50, required=True, label="$500 Answer", widget=forms.TextInput(attrs={'placeholder': 'Answer...'}) )
