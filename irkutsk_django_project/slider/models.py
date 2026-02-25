from django.db import models

# # Create your models here.
# from django.db import models
# from filer.fields.image import FilerImageField
# from adminsortable2.models import SortableMixin

# class SliderImage(SortableMixin):
#     title = models.CharField('Название', max_length=255)
#     image = FilerImageField(
#         verbose_name='Изображение',
#         on_delete=models.CASCADE,
#         related_name='slider_images'
#     )
#     is_active = models.BooleanField('Активно', default=True)
#     order = models.PositiveIntegerField('Порядок', default=0, editable=False, db_index=True)

#     class Meta:
#         verbose_name = 'Изображение для слайдера'
#         verbose_name_plural = 'Изображения для слайдера'
#         ordering = ['order']

#     def __str__(self):
#         return self.title
