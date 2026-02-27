from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'is_active', 'order']
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    list_per_page = 20

    def image_preview(self, obj):
        """Показывает миниатюру изображения в админке"""
        if obj.image:
            # Создает миниатюру 100x50 на лету
            thumbnailer = get_thumbnailer(obj.image)
            thumbnail = thumbnailer.get_thumbnail(
                {
                    'size': (100, 50),  # Размер миниатюры
                    'crop': 'smart',  # Умная обрезка
                    'quality': 90,  # Качество 90%
                }
            )
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px; border-radius: 4px;">',
                thumbnail.url,  # Ссылка на миниатюру
            )
        return format_html('<span style="color: #999;">Нет изображения</span>')

    image_preview.short_description = 'Превью'
