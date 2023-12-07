from django import forms
from .models import Fooditems 

class AddFoodItems(forms.ModelForm):
    class Meta:
        model = Fooditems
        fields = ["name", "calories", "ucalories"]
        # "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'calories' : forms.TextInput(attrs={'class': 'form-control'}),
            'ucalories' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'user' : forms.Select(attrs={'class': 'form-control'})
        }

# class uForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = "__all__"
#         # ["uName", "email", "password", "userFkey"]
#         widgets = {
#             'name' : forms.TextInput(attrs={'class': 'form-control'}),
#             'email' : forms.TextInput(attrs={'class': 'form-control'}),
#             'password' : forms.TextInput(attrs={'class': 'form-control'}),
#             # 'userFkey' : forms.Select(attrs={'class': 'form-control'}),
#         }
    
