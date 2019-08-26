from django import forms
from django.contrib.auth.models import *
from django.contrib.auth.models import User
#from .models import User
from .models import Subscribe,Callback
from django.contrib.auth import get_user_model
User = get_user_model()
class UserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('password','username','first_name','numberphone')
		# fields = ('__all__')

class SubForm(forms.ModelForm):
	
	class Meta:
		model = Subscribe
		fields = ('__all__')

class CallForm(forms.ModelForm):
	
	class Meta:
		model = Callback
		fields = ('__all__')