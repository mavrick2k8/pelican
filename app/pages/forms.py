from django import forms
from .models import * 

class FaqForm(forms.ModelForm):
	
	class Meta:
		model = Faq
		fields = ('question','e_mail','name')