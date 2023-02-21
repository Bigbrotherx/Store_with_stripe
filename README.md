# Store with "Stripe"

## Ознакомится с примером можно [здесь](https://bigbrotgerx.pythonanywhere.com)

* Сценарии работы:
  * Сразу заказать выбранный товар нажав кнопку "Купить"
  * Собрать заказ добавив нужные товары кнопкой "Добавить в корзину" -> Когда все товары добавлены нажать кнопку "Оформить заказ":
    * Чтобы на странице заказа применить скидку введите промокод **`SALE20`**
    * Нажмите кнопку "Оплатить"

## Инструкция по установке

1. Установить вирутальное окружение:
   * Пример для Linux

   ```python
     $  python3.9 -m pip install venv venv
   ```
2. Активировать окруженин и установить требующиеся зависимости:
   * Пример для Linux

   ```python
     $ source venv/bin/activate
     (venv)$ pip install -r requiments.txt
   ```
3. Запустить сервер
   * Пример для Linux

   ```python
     <project_dir>store_with_stripe/my_store(venv)$ python manage.py runserver
   ```

## Администрирование

В проекте настроенны модели [админки](https://bigbrotgerx.pythonanywhere.com/admin/). Для получения доступа используйте:

```python
	   Login: ruzzik
       password: admin
	```
  
```
