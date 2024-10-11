from django import forms

class Employ_form(forms.Form):
    
    emp_id = forms.IntegerField()
    emp_name = forms.CharField(max_length = 100)
    emp_desg = forms.CharField(max_length = 100)