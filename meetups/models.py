from django.db import models
from django.utils.timezone import now


# Create your models here.
class Location(models.Model):
    name = models.CharField(
        max_length=200
    )
    address = models.CharField(
        max_length=300
    )

    def __str__(self):
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    email = models.EmailField(
        unique=True
    )

    def __str__(self):
        return f"{self.email}"


class Meetup(models.Model):
    title = models.CharField(
        max_length=200
    )
    organizer_email = models.EmailField()
    date = models.DateField()

    slug = models.SlugField(
        unique=True
    )
    description = models.TextField(
    )
    image = models.ImageField(
        upload_to="uploads/meetups"
    )
    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE,
        related_name="meetups",
        blank=True
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )

    participants = models.ManyToManyField(
        to=Participant,
        blank=True
    )

    def __str__(self):
        return f'{self.title}'
