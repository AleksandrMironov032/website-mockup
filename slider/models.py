from django.db import models
from filer.fields.image import FilerImageField


class Slide(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        verbose_name='Фотография',
        related_name='slides'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        db_index=True
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title