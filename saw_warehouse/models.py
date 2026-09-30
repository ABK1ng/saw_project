from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=200, verbose_name="Маркировка / Размер")
    quantity = models.PositiveIntegerField(verbose_name="Количество (шт)")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее обновление")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.name} ({self.total_length} м, {self.quantity} шт)"

    @property
    def total_length(self):
         return self.quantity * 6