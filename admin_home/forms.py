from django import forms
class Add_product_form(forms.Form):
    name=forms.CharField(max_length=50)
    price=forms.FloatField()
    description=forms.CharField(max_length=10000)
    category=forms.CharField(max_length=50)
    product_img=forms.ImageField(required=False)