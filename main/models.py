from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            )
    slug = models.SlugField(max_length=150,
                            unique=True,
                            db_index=True,
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True,
                            )
    slug = models.CharField(max_length=150,
                            db_index=True,
                            )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                )
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='images-products',
                              blank=True,
                              )
    category = models.ForeignKey(Category,
                                 related_name='Produtos',
                                 null=True,
                                 on_delete=models.CASCADE,
                                 )

    def __str__(self) -> str:
        return self.name
