from django.utils import timezone
from django.db import models

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KI", "KIWI"),
        ("EL", "ELAICHI"),
        ("PL", "PLAIN"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")  # Must be a string
    created_at = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
