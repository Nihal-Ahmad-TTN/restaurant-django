from django import forms
from .models import Manager, Menu 

class LoginForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'
        labels = {'manager_name' : "enter your name",
                  'manager_email' : "enter your email",
                  'manager_city' : "enter your city",
                  'manager_phone' : "enter your phone",
                  'manager_password' : 'enter your password',
                  }
        
class AddMenu(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['food_name', 'food_desc', 'food_category', 'food_type', 'food_price', 'food_image']
        widgets = {
             'food_name' : forms.TextInput(attrs={'class' : "mail_text", 'placeholder': "Enter Food Name"}),
             'food_desc' : forms.TextInput(attrs={'class' : "mail_text", 'placeholder': "Enter Food Description"}),
             'food_category' : forms.Select(attrs={'class' : "mail_text"}),
             'food_type' : forms.Select(attrs={'class' : "mail_text"}),
        }
        labels = {'food_name' : "",
                  'food_desc' : "",
                  }

    


