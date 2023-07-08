from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.forms import CookCreateForm
from kitchen.models import DishType, Dish, Cook


class FormsTests(TestCase):
    def test_cook_creation_form(self):
        form_data = {
            "username": "new_user",
            "password1": "test123test",
            "password2": "test123test",
            "first_name": "Test",
            "last_name": "Test",
            "years_of_experience": 10
        }
        form = CookCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class SearchFormTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_dish_type_search(self):
        request = "Test"
        response = self.client.get(f"/dish_types/?name={request}")
        queryset = response.context["dish_type_list"]
        expected_queryset = DishType.objects.filter(
            name__icontains=request
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(queryset),
            list(expected_queryset))

    def test_dish_search(self):
        request = "Test"
        response = self.client.get(f"/dishes/?name={request}")
        queryset = response.context["dish_list"]
        expected_queryset = Dish.objects.filter(
            name__icontains=request
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(queryset),
            list(expected_queryset))

    def test_cook_search(self):
        request = "Test"
        response = self.client.get(f"/cooks/?name={request}")
        queryset = response.context["cook_list"]
        expected_queryset = Cook.objects.filter(
            username__icontains=request
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(queryset),
            list(expected_queryset))
