from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)
    category_image = models.ImageField(upload_to='lib/static/Categories_images')

    def __str__(self):
        return self.category

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='lib/static/Books_covers')
    location = models.CharField(max_length=250)
    publish_date = models.DateField()
    Edition = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
    availability = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.name