from django import forms

from PythonWebBasicsRetakeExam19April2022.profile_app.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ('first_name', 'last_name', "profile_picture")
        widgets = {
            'password': forms.PasswordInput()
        }
