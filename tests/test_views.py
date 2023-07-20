from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType

COOK_URL = reverse("kitchen:cook-list")
DISH_URL = reverse("kitchen:dish-list")
DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "password111")
        self.client.force_login(self.user)


class PublicTests(TestCase):
    def test_cook_list_login_required(self):
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_dish_list_login_required(self):
        response = self.client.get(DISH_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_dish_type_list_login_required(self):
        response = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTest(BaseTestCase):
    def test_create_cook(self):
        form_data = {
            "username": "new_user",
            "password1": "test123test",
            "password2": "test123test",
            "first_name": "Test",
            "last_name": "Test",
            "years_of_experience": 10
        }
        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])


class PrivateDishTest(BaseTestCase):
    def test_retrieve_dish(self):
        response = self.client.get(DISH_URL)
        dishes = Dish.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")


class PrivateDishTypeTest(BaseTestCase):
    def test_retrieve_dish_type(self):
        DishType.objects.create(name="Test")
        response = self.client.get(DISH_TYPE_URL)
        dish_types = DishType.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

