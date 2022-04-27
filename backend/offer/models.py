from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Offer(models.Model):
    bank_name = models.CharField(max_length=40)
    term_min = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    term_max = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    rate_min = models.FloatField(
        validators=[MinValueValidator(0.0001)]
    )
    rate_max = models.FloatField(
        validators=[MaxValueValidator(100.0)]
    )
    payment_min = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    payment_max = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        ordering = ('rate_min', )
