from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

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


# relations

# one to many

class ChaiReviews(models.Model):
    RATING_CHOICE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} for chai {self.chai.chai_type}'


# many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name
    
# one to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100, )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'certificate for {self.chai.name}'