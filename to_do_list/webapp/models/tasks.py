from django.db import models
from django.utils import timezone



class Tasks(models.Model):
    task = models.CharField(
        max_length=100, blank=False, 
        null=False, 
        verbose_name='Краткое описание'
        )
    description = models.TextField(
        max_length=3000, 
        blank=True, 
        null=True, 
        default=' ', 
        verbose_name='Полное описание'
        )
    project = models.ForeignKey(
        to='webapp.Projects',
        verbose_name='Проект',
        related_name='tasks',
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        to='webapp.Statuses',
        verbose_name='Статус задачи',
        related_name='statuses',
        on_delete=models.RESTRICT
    )
    type = models.ManyToManyField(
        to='webapp.Types',
        verbose_name='Тип задачи',
        related_name='types'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания', 
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Время изменения'
        )
    deleted_at = models.DateTimeField(
        verbose_name='Дата удаления', 
        null=True, 
        default=None
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено', 
        default=False, null=False
    )

    def __str__(self) -> str:
        return f'{self.task} - {self.description} - {self.type} - {self.status}'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()