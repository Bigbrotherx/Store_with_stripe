# Generated by Django 4.1.7 on 2023-02-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['price'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте изображение к посту', upload_to='items/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'Доллары США'), ('rub', 'Росийский Рубль'), ('eur', 'ЕВРО'), ('czk', 'Чешская Крона'), ('uah', 'Украниская Гривна')], help_text='Выберите валюту', max_length=3, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(help_text='Опишите товар'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=0, help_text='Укажите цену товара', max_digits=20, verbose_name='Цена товара'),
        ),
    ]
