from django.forms import ModelForm
from chats.models import Session, Chat


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['question']
