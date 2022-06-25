from django.test import TestCase


# Create your tests here.
class PageTemplateRenderTest(TestCase):
    # def test_for_homepage(self):
    #     response = self.client.get("")
    #     self.assertTemplateUsed(response, "homepage.html")

    def test_for_login_page(self):
        response = self.client.get("/login")
        self.assertTemplateUsed(response, "login_page.html")

    # def test_for_donate(self
    #     response = self.client.get("/donate")
    #     self.assertTemplateUsed(response, "donate.html")
