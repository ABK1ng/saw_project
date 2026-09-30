from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "get_total_length", "quantity", "updated_at")
    search_fields = ("name",)
    list_filter = ("updated_at",)
    list_editable = ("quantity",)

    @admin.display(description="Общая длина (М)")
    def get_total_length(self, obj):
        return obj.total_length