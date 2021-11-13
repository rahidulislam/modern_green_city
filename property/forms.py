from django import forms
from django.db.models.query import QuerySet
from property.models import Katha, Land, LandQuery, Plot, Side
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row,Column,Layout,Submit

class AddLandQueryForm(forms.ModelForm):
    land = forms.ModelChoiceField(label='', queryset=Land.objects.all(), empty_label='Select Land')
    katha = forms.ModelChoiceField(label='', queryset=Katha.objects.all(), empty_label='Select Katha')
    side = forms.ModelChoiceField(label='', queryset=Side.objects.all(), empty_label='Select Side')
    plot = forms.ModelChoiceField(label='', queryset=Plot.objects.all(), empty_label='Select Plot')
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Name'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Phone'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    job_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter Job Title'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Message', 'rows':'3'}))
    class Meta:
        model = LandQuery
        fields = "__all__"

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('land', css_class='form-group col-md-4 mb-0'),
                Column('katha', css_class='form-group col-md-4 mb-0'),
                Column('side', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('plot', css_class='form-group col-md-4 mb-0'),
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('job_title', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('message', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Search', css_class='search-btn')
            
        )
    

        
