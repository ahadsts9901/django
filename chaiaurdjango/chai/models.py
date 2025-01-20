from django.utils import timezone
from django.db import models

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KI", "KIWI"),
        ("EL", "ELAICHI"),
        ("PL", "PLAIN"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    created_at = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)