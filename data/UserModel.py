from tortoise import fields
from tortoise.models import Model


class UserState(Model):
    id = fields.IntField(pk=True)  # is recommended
    uid = fields.IntField()
    branch = fields.CharField(20)
    context = fields.CharField(255)

    class Meta:
        database = "user_state"
