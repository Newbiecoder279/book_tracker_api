from django.db import models

# Create your models here.
class Book(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing','Ongoing')
    ]
    RATING_CHOICES = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default="ongoing")
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title