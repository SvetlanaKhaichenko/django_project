from django.core.management import BaseCommand

from recipesapp.models import RecipeCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = [
            "Первые блюда",
            "Вторые блюда",
            "Закуски",
            'Салаты',
            'Соусы,'
            ' кремы',
            'Напитки',
            "Десерты",
            "Выпечка",
            "Безглютеновая выпечка",
            "Торты",
            "Заготовки на зиму",
            "Блюда в мультиварке",
            "Полезные мелочи"
        ]

        for category in categories:
            category, created = RecipeCategory.objects.get_or_create(name=category)
            self.stdout.write(self.style.SUCCESS(f'Category {category}'))