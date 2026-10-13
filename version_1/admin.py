from django.contrib import admin
from version_1.models import MenuItems
from version_1.models import BusinessHours
from version_1.models import BusinessSettings
# Register your models here.
admin.site.register(MenuItems)

@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    list_display = ('day', 'opening_time', 'closing_time', 'is_closed')

admin.site.register(BusinessSettings)