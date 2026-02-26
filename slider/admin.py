from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Slide


@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'preview_image', 'title')
    list_display_links = ('title',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 60px; border-radius: 4px;" />',
                obj.image.url
            )
        return '—'

    preview_image.short_description = 'Фото'