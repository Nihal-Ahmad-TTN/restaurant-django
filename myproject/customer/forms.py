from django import forms
from management.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=255, label='' , widget=forms.PasswordInput(attrs={'class' : "mail_text", 'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(max_length=255, label='', widget=forms.PasswordInput(attrs={'class' : "mail_text", 'placeholder': 'Confirm Password', 'style':'margin-bottom: 20px;'}))

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password']
        widgets = {
             'name' : forms.TextInput(attrs={'class' : "mail_text", 'placeholder': 'Enter Name'}),
             'email' : forms.EmailInput(attrs={'class' : "mail_text", 'placeholder': 'Enter Email'}),
        }
        labels = {'name' : "",
                  'email' : "",
                  }
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password',"Password does not match")
        elif len(password) < 8:
             self.add_error("password must be 8 characters long")
        return cleaned_data
    
    
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
        
        

