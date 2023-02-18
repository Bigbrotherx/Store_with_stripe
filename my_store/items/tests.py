from http import HTTPStatus
import shutil
import tempfile

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Item


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ItemViewTests(TestCase):
    '''Класс тестов приложения Items'''
    @classmethod
    def setUpClass(cls):
        '''Фикстуры класса'''
        super().setUpClass()
        byte_image = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
        cls.image = SimpleUploadedFile(
            name='test_image.gif',
            content=byte_image,
            content_type='image/gif'
        )
        Item.objects.bulk_create([
            Item(
                name='Тестовый товар',
                description='Тестовое описание',
                price=100,
                currency='usd',
                image=cls.image,
            ) for _ in range(5)
        ])
        cls.items = Item.objects.all()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_items_uses_correct_template(self):
        """Главная страница использует корректный шаблон"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'items/index.html')

    def test_index_shows_correct_context(self):
        '''Проверка контекста главной страницы'''
        response = self.client.get(reverse('items:index'))
        item = response.context['items'][0]
        self.assertEqual(item.id, ItemViewTests.items[0].id)
        self.assertEqual(item.name, ItemViewTests.items[0].name)
        self.assertEqual(item.description, ItemViewTests.items[0].description)
        self.assertEqual(item.price, ItemViewTests.items[0].price)
        self.assertEqual(item.currency, ItemViewTests.items[0].currency)
