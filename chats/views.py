import openai

from django.views import generic

from chats.forms import ChatForm
from chats.models import Session, Chat

SAMPLE_QUESTIONS = [
    '''鸦片战争的主要原因是什么？它如何影响中国与西方列强的关系？''',
    '''中国历史问题'''
]

openai.api_key = "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"


class HomeView(generic.FormView):
    template_name = 'index.html'
    form_class = ChatForm
    success_url = '/'

    def form_valid(self, form):
        question = self.request.POST.get('question')
        session = Session.get_valid()
        answer = self.get_answer(question, session)
        Chat.objects.create(question=question, answer=answer, session=session)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        Session.objects.create()
        return super().form_invalid(form)
    
    def get_answer(self, txt, session):
        command = ''
        for chat in session.chat_set.all():
            command += f'{chat.question}\n\n{chat.answer}'
        command += f'\n\n\n\n{txt}?'
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=txt,
            temperature=0.1,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text.strip()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = Session.objects.first()

        if session:
            chat = session.chat_set.first()
            if chat:
                context['chat'] = chat.answer
        context['session'] = session if session else []


        return context
