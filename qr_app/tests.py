from django.test import TestCase


class GenerateQRCodeViewTests(TestCase):
    def test_invalid_post_renders_form_errors(self):
        response = self.client.post(
            "/",
            {"restaurant_name": "Cafe", "menu_url": "not-a-url"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("menu_url", response.context["form"].errors)
