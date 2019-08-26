from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
class BasketAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	price = forms.IntegerField()
	product = forms.CharField(required=False,max_length=150)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)