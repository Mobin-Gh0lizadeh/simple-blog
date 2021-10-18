from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)
		widgets = {'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'text'})}
		error_messages = {'body':{'required': 'comment not be blanck'}}
		help_texts = {'body':'max 500 char'}