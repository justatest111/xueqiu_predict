from django.contrib import admin
from models import Stock
# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'stock_number',
        'followers_number',
        'new_followers_number',
        'value_increased_percent',
        'update_time'
    )
        
        
        
        
#  admin.site.register(Stock, StockAdmin)
