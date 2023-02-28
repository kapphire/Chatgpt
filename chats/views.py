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
    
    def get_answer(self, prompt, session):
        context = ''
        for chat in session.chat_set.order_by('created')[:5]:
            # context += f'{chat.question}\n{chat.answer}\n'
            context += f'{chat.question}\n'

        print(context)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="context:" + context + "\n\n" + "prompt:" + prompt,
            max_tokens=4000,
            temperature=0.7,
            top_p=1,
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
