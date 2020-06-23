from django import forms
from django.forms import ModelForm
from .models import user_upload_notes

class userForm(forms.ModelForm):
	class Meta:
		model= user_upload_notes
		fields={
			'email',
			'branch',
			'semester',
			'ufile',
			'text',
			

		}
		widgets = {'text': forms.Textarea(attrs={'row': 3, 'col': 3}),}			