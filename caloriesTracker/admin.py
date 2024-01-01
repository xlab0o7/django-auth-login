from django.contrib import admin
from .models import ListFoodItems, DailyFoodInTake

# Register your models here.
admin.site.register(ListFoodItems)
admin.site.register(DailyFoodInTake)

# class trackerAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'itemname',
#         'user_calories',
#         'total_cal_day',
#         'status'
#         ]