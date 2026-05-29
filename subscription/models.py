from django.db import models

# Create your models here.

class Subscription(models.Model):

    name = models.CharField(
        max_length=20,
        default='BASIC',
    )

    days = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subscription'


class GymMemberShip(models.Model):
    trainer = models.ForeignKey('trainer.Trainer', on_delete=models.CASCADE, null=True, blank=True)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    subsrciption = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subsrciption

    class Meta:
        db_table = "gymmembership"

