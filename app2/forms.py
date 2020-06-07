from django import forms

choice=[('atul','Atul'),('priya','priya'),('nisha','Nisha')]
class inputdata(forms.Form):
    first_name = forms.CharField( max_length = 200, widget=forms.Select(choices=choice))
    address = forms.CharField( max_length = 200)
    salary=forms.IntegerField(help_text='enter the salary')
    status=forms.BooleanField()


