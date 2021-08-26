from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
		
class SubredditForm(forms.ModelForm):
	class Meta:
		model = SubReddit
		fields = ('name','cover_image_url')

class PostForm(forms.ModelForm):
    subreddits = forms.ModelMultipleChoiceField(queryset=SubReddit.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'text', 'url', 'subreddits')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class SearchForm(forms.Form):
    query = forms.CharField(label='Query', required=False)