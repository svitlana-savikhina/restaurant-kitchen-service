from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="test.admin",
            password="FGh12j33"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="test",
            password="test111",
            years_of_experience=10
        )

    def test_cook_years_of_experience(self):
        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)
