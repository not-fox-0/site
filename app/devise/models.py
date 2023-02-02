from audioop import reverse
from django.db import models
from django.template.defaultfilters import slugify



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    has_rgb = models.BooleanField(default=False)
    product_img = models.ImageField(upload_to='')

    def __str__(self):
        return f"{self.product_img} {self.name} {self.description} {self.slug} {self.price} {self.has_rgb}"

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return f'{self.username} {self.comment}'