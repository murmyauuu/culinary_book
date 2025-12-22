from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cooking_time_minutes = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    original_recipe = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="variations",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def is_variation(self):
        return self.original_recipe is not None


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    amount = models.CharField(max_length=50, blank=True)
    note = models.CharField(max_length=100, blank=True)


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ["number"]