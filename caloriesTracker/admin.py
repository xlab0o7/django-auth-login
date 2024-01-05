from django.contrib import admin
from .models import DailyFoodTake

# Register your models here.
# admin.site.register(ListFoodItems)
# admin.site.register(DailyFoodInTake)

# class trackerAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'itemname',
#         'user_calories',
#         'total_cal_day',
#         'status'
#         ]


@admin.register(DailyFoodTake)
class DailyFoodAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'food_items'
    ]
