from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        name_ = DishType.objects.create(name="test")
        self.assertEqual(str(name_), name_.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test111",
            first_name="Test first",
            last_name="Test last"
        )
        self.assertEqual(str(cook), f"{cook.username} ({cook.first_name} {cook.last_name})")

    def test_get_absolute_url(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test111"
        )
        expected_url = f"/cooks/{cook.pk}/"
        self.assertEqual(cook.get_absolute_url(), expected_url)

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Main")
        name = Dish.objects.create(name="test", price=10.99, dish_type=dish_type)
        self.assertEqual(str(name), name.name)
