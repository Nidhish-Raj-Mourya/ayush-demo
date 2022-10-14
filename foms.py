from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	f_name = forms.CharField(label="First Name", max_length=15)
	l_name = forms.CharField(label="Last Name", max_length=15)


	class Meta:
		model = User
		fields = ('username', 'f_name','l_name','email', "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user