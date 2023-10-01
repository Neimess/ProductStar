from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Subsidiary(models.Model):
    address = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            )
    floor = models.IntegerField(null=False,
                                blank=False,
                                )
    subsidiary = models.ForeignKey("employees.Subsidiary",
                                   null=True,
                                   related_name="departments",
                                   on_delete=models.SET_NULL,
                                   )


class Employee(models.Model):
    full_name = models.CharField(max_length=255,
                                 null=False,
                                 blank=False,
                                 )
    position = models.CharField(max_length=255,
                                null=False,
                                blank=False,
                                )
    phone_number = PhoneNumberField(null=True,
                                    blank=True)
    birth_date = models.DateField(null=True,
                                  blank=True)
    email = models.EmailField(null=True,
                              blank=True,
                              )
    department = models.ForeignKey("employees.Department",
                                   null=True,
                                   related_name="employees",
                                   on_delete=models.CASCADE,
                                   )

    def __repr__(self) -> str:
        return f"{self.full_name}"
