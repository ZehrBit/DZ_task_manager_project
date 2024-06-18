from django.db import models


class MyTask(models.Model):
    PRIORITY_CHOICES = (
        ('высокий', 'Высокий'),
        ('средний', 'Средний'),
        ('низкий', 'Низкий'),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    note = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ----- Автор: {self.author} ----- Приоритет: {self.priority} ----- Статус: {self.status}"
