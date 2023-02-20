from django.db import models
from django.core.exceptions import ValidationError


CURRENCIES = (
    ('usd', 'Доллары США'),
    ('rub', 'Росийский Рубль'),
    ('eur', 'ЕВРО'),
    ('czk', 'Чешская Крона'),
    ('uah', 'Украниская Гривна'),
)

DURATIONS = (
    ('once', 'Разовый'),
    ('forever', 'Постоянный'),
    ('repeating', 'Повторяющийся'),
)


def percent_off_validation(value):
    """Проверка что процент скидки в промежутке 1-100"""
    if 1 <= value < 100:

        return value
    else:
        raise ValidationError('Скидка должна быть в диапозоне 1-100')


class Discount(models.Model):
    code = models.CharField('Промокод', max_length=10, unique=True)
    discount_name = models.CharField('Уникальное имя', max_length=50)
    discount_id = models.CharField('Id в системе stripe',
                                   max_length=50, blank=True, null=True)
    percent_off = models.PositiveSmallIntegerField(
        'Процент скидки',
        validators=[percent_off_validation]
    )
    duration = models.CharField(
        'Продолжительность',
        max_length=15,
        choices=DURATIONS
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'discount_name'],
                name='unique_discount',
            )
        ]
        ordering = ['percent_off']
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Item(models.Model):
    name = models.CharField('Название', max_length=250)
    product_id = models.CharField(
        'ID в платежной системе',
        max_length=50,
        blank=True,
        null=True
    )
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


class Order(models.Model):
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='orders')
    items = models.ManyToManyField(
        Item,
        related_name="order",
        through='ItemOrder'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        """Информация о заказе"""

        return f'{self.items}'


class ItemOrder(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='item_order')
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_item')
