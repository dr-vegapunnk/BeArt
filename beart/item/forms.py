from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'
class newItemForm(forms.ModelForm): #
    class Meta:
        model = Item               #model = Item: Indicates that this form is associated with the Item model.
        fields = ('Category','name','description','price','image','id_sold')
                                    # Specifies which fields from the Item model should be included in the form.
        widgets = {
            'Category': forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('Category','name','description','price','image','id_sold')
    
        widgets = {
            'Category': forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }