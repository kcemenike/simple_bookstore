from django.test import TestCase
from main import models
from django.core.files.images import ImageFile
from decimal import Decimal


class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        product = models.Product(
            name='Learning Python 3.8',
            price=Decimal("20.00"),
        )
        product.save()

        # input("press any key to continue")

        with open("main/fixtures/learning-python-38.jpg", "rb") as f:
            image = models.ProductImage(
                product=product, image=ImageFile(f, name="lp38.jpg"),)
            with self.assertLogs("main", level="INFO") as cm:
                image.save()

        self.assertGreaterEqual(len(cm.output), 1)
        image.refresh_from_db()

        with open("main/fixtures/learning-python-38-thumb.jpg", "rb",) as f:
            expected_content = f.read()
            print(type(expected_content))
            assert image.thumbnail.read() == expected_content

        image.thumbnail.delete(save=False)
        image.image.delete(save=False)
