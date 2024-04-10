from django.test import TestCase
from .views import zodiac_dict


# тесты именно для приложения
class TestHoroscope(TestCase):

    def test_main_page(self):
        response = self.client.get('/horoscope/type/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())


    def test_libra_redirect(self):
        lst = list(zodiac_dict)
        for i in range(1, 13):
            response = self.client.get(f'/horoscope/{i}/')
            self.assertEqual(response.status_code, 301)
            self.assertEqual(response.url, f'/horoscope/{lst[i - 1]}/')