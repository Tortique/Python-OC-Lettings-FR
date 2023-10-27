from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    A model to represent an address with the following fields:

    Attributes:
        number (models.PositiveIntegerField): The street number (up to 9999).
        street (models.CharField): The name of the street (up to 64 characters).
        city (models.CharField): The city name (up to 64 characters).
        state (models.CharField): The state abbreviation (2 characters) with a minimum length validator.
        zip_code (models.PositiveIntegerField): The ZIP code (up to 99999).
        country_iso_code (models.CharField): The ISO country code (3 characters) with a minimum length validator.

    Methods:
        __str__(): Returns a string representation of the address, combining the number and street.

    Meta:
        verbose_name_plural = "Addresses"
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model to represent a letting or rental property.

    Attributes: title (models.CharField): The title of the letting (up to 256 characters). address (
    models.OneToOneField): A one-to-one relationship with the Address model, linking the letting to an address.

    Methods:
        __str__(): Returns a string representation of the letting, which is the title of the property.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
