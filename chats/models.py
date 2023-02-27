from datetime import datetime, timedelta
from django.db import models
from django.utils.timezone import now

class Session(models.Model):
    archived = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f'Session {self.pk}'

    @classmethod
    def get_valid(cls):
        if not cls.objects.count():
            return cls.objects.create()

        session = cls.objects.first()
        print(now() - timedelta(minutes=5))
        print(session.updated)
        if now() - timedelta(minutes=5) < session.updated:
            session.save()
            return session

        return cls.objects.create()


class Chat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f'Chat {self.question}'
