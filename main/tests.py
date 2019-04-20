import io
from PIL import Image

from django.urls import reverse
from rest_framework.test import APITestCase


class ImagesAPIViewTestCase(APITestCase):
    get_url = reverse("get_images")
    post_url = reverse("post_image")
    image_path = 'media/images/test.jpg'

    def test_get(self):
        response = self.client.get(self.get_url)
        self.assertEqual(200, response.status_code)

    def test_post(self):
        response = self.client.post(self.post_url,
                                    data={'content': self.generate_photo_file(),
                                          'place': 'Россия'})
        self.assertEqual(200, response.status_code)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(10, 10), color=(255, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
