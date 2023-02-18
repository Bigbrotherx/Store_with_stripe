from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CURRENCIES = (
    ('usd', 'Доллары США'),
    ('rub', 'Росийский Рубль'),
    ('eur', 'ЕВРО'),
    ('czk', 'Чешская Крона'),
    ('uah', 'Украниская Гривна'),
)


class Item(models.Model):
    name = models.CharField('Название', max_length=250)
    description = models.TextField(help_text='Опишите товар')
    price = models.DecimalField(
        'Цена товара',
        max_digits=20,
        decimal_places=0,
        help_text='Укажите цену товара')
    currency = models.CharField(
        'Валюта',
        max_length=3,
        choices=CURRENCIES,
        help_text='Выберите валюту',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='items/',
        blank=True,
        help_text='Добавьте изображение к посту',
    )

    class Meta:
        ordering = ['price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        """Информация о товаре"""

        return f'{self.name} по цене:{self.price/100:.2f}{self.currency}'
