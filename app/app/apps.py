from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

class ProductConfig(AppConfig):
    name = 'Продукты'
    verbos_name = "Список продуктов"
