from django import forms

from company.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        
        
class BadgesForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        
        
class MapDataForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"