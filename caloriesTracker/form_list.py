from django import forms
from caloriesTracker.models import ListFoodItems


class AddItemsFood(forms.ModelForm):
    class Meta:
        model = ListFoodItems
        fields = ['names', 'calories', 'List']

        widgets = {
            'names': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.TextInput(attrs={'class': 'form-control'}),
            # 'ucalories' : forms.TextInput(attrs={'class': 'form-control'}),
            'List': forms.Select(attrs={'class': 'form-control'})
        }
