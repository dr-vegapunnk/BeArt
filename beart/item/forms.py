from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'
class newItemForm(forms.ModelForm): #
    class Meta:
        model = Item               #model = Item: Indicates that this form is associated with the Item model.
        fields = ('Category','name','description','price','image',)
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','id_sold')
    
        widgets = {
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