from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "cooking_time_minutes"]

    def clean_cooking_time_minutes(self):
        value = self.cleaned_data.get("cooking_time_minutes")
        if value and value < 1:
            raise forms.ValidationError("Время приготовления должно быть положительным числом.")
        return value

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise forms.ValidationError("Название должно содержать не менее 3 символов.")
        return title