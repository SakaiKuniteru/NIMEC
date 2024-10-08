from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=225)
    image_book = models.ImageField(upload_to='book/images/')
    book_description = models.TextField()
    author = models.CharField(max_length=225)
    release_date = models.DateField()
    book_price = models.DecimalField(max_digits=12, decimal_places=0)

    def formatted_price(self):
        return "{:,.0f}".format(self.book_price).replace(',', '.')

    def __str__(self):
        return self.book_name