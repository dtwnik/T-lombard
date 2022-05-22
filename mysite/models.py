import os
from django.db import models
from twilio.rest import Client


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    small_image = models.URLField(null=True)
    metall = models.CharField(max_length=30, null=True)
    vstavka = models.CharField(max_length=30, null=True)
    proba = models.CharField(max_length=30, null=True)
    weight = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=30, null=True)
    style = models.CharField(max_length=30, null=True)


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'ACbde8e8f51b3c68c933a26d98fabad85c'
            auth_token = 'b55a7c7f68dc90de2abe3c1495e0f04d'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='+19782917759',
                    to='+77086033589'
            )
            print(message.sid)
        return super().save(*args, **kwargs)