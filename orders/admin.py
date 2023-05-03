from django.contrib import admin
from .models import Order, OrderItem


class TabularOrderItem(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'adress',
                    'number',
                    'neighborhood',
                    'city',
                    'complement',
                    'state',
                    'postal',
                    'created_at',
                    'paid_out',
                    ]
    list_filter = ['paid_out',
                   'created_at',
                   'name',
                   ]
    inlines = [TabularOrderItem]
