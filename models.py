from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime

class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.CharField(max_length=100, null=False)
    is_verified = fields.BooleanField(default=False)
    join_data = fields.DatetimeField(default=datetime.now)

class Business(Model):
    id = fields.IntField(pk=True, index=True)
    business_name = fields.CharField(max_length=20, null=False, unique=True)
    city = fields.CharField(max_length=100, null=False)
    business_description = fields.TextField(null=True)
    logo = fields.CharField(max_length=200, null=False, default="default.jpg")
    owner = fields.ForeignKeyField("models.User", related_name="business")

class Product(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=20, null=False, unique=True)