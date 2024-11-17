from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории для рецептов'

class Recipe(models.Model):
    category = models.OneToOneField(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    Name = models.CharField(
        max_length=155,
        verbose_name='Название рецепта'
    )
    ingredients = models.TextField(
        verbose_name='Список ингрендиентов'
    )
    instructions = models.TextField(
        verbose_name='Инструкция по приготовлению '
    )
    prep_time = models.IntegerField(
        verbose_name='Время приготовления'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления рецепта'
    )
    is_vegeterian = models.BooleanField(
        default=False,
        verbose_name='Вегетарианское блюдо'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Рецепты'