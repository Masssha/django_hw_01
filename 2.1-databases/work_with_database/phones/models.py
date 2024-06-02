from django.db import models
# from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField()
    release_date = models.DateField
    lte_exists = models.BooleanField
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
    # TODO: Добавьте требуемые поля
    # pass
