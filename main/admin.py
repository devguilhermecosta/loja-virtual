from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", ]
    list_display_links = ["id", "name", "slug", ]
    list_filter = ["name", ]
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ["name", ]
    ordering = ["-id"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "stock",
        "available",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "available",
        "created_at",
        "updated_at",
        ]
    list_editable = [
        "price",
        "stock",
        "available",
    ]
    prepopulated_fields = {'slug': ('name',)}
