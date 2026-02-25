from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage
from django.utils.html import format_html


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'is_active', 'order']
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    list_per_page = 20
    readonly_fields = ['created_at', 'updated_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px; border-radius: 4px;">',
                obj.image.url,
            )
        return format_html('<span style="color: #999;">Нет изображения</span>')

    image_preview.short_description = 'Превью'
