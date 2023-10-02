from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.


class ApiUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USER_TYPES = [
        ("supplier", "Поставщик"),
        ("consumer", "Потребитель"),
    ]
    user_type = models.CharField(choices=USER_TYPES, max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Repository(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"""Repositories' name is  {self.name},
                        located at {self.location}"""


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,
                                   blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    repository = models.ForeignKey(Repository,
                                   related_name="items",
                                   on_delete=models.CASCADE,
                                   db_column="repository_id")

    def __str__(self) -> str:
        return f"{self.name}, repositories have a {self.quantity} objects"


class Order(models.Model):
    quantity = models.IntegerField()
    orderer = models.ForeignKey(ApiUser,
                                related_name="users",
                                on_delete=models.CASCADE,
                                db_column="orderer_id")
    item = models.ForeignKey(Item,
                             related_name="orders",
                             on_delete=models.CASCADE,
                             db_column="item_id")
    repository = models.ForeignKey(Repository,
                                   related_name="orders",
                                   on_delete=models.CASCADE,
                                   db_column="repository_id")
