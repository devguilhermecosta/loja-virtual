from django.db import models
from django.urls import reverse


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

    class Meta:
        ordering = ('name', )
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('main:products_list_filter',
                       args=(self.slug,),
                       )


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
    cover = models.ImageField(upload_to='images-products/',
                              blank=True,
                              )
    category = models.ForeignKey(Category,
                                 related_name='Produtos',
                                 null=True,
                                 on_delete=models.CASCADE,
                                 )

    class Meta:
        ordering = ['name']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        indexes = [
            models.Index(
                fields=['id', 'slug'],
                name='idx_slug',
            )
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            'main:product_detail',
            args=(self.id, self.slug),
            )
