from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    """
    Форма для создания и редактирования материала.
    Django сам возьмет правила из модели Material.
    """
    class Meta:
        model = Material          # Указываем, с какой моделью работаем
        fields = ['name', 'quantity'] # Указываем, какие поля можно заполнять
        
        # (Опционально) Можно добавить подсказки или изменить типы полей прямо здесь:
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Например: Труба 40x20x2'}),
            'quantity': forms.NumberInput(attrs={'min': '1'}),
        }