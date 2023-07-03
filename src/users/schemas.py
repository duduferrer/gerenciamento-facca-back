from ninja import ModelSchema
from .models import User


class UserSchemaOnList(ModelSchema):
    class Config:
        model = User
        model_fields = ["first_name", "last_name",
                        "is_active", "role", "balance"]


class UserInputSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ["username", "first_name", "last_name",
                        "password", "fastbuy_code", "email"]

class UserOutputSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ["username", "first_name", "last_name",
                        "balance", "fastbuy_code", "email", "is_active", ]
