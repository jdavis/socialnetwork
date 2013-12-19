from datetime import datetime

from django.shortcuts import render

from messages.models import Message, MessageForm


def messages(request):
    context = {}
    context['messages'] = dummy_data

    message = Message()
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        form.sender = request.user
        form.save()
    else:
        form = MessageForm(request.POST, instance=message)

    context['message_form'] = form
    context['current_thread'] = 'Shredder'
    context['threads'] = dummy_data.keys()
    context['messages'] = dummy_data['Shredder']

    return render(request, 'messages/index.html', context)

def post(request):
    pass


dummy_data = {
    'Shredder': [
        {
            'sent': False,
            'content': 'Hey there Donatello. Want to go out and get some pizza?',
            'viewed': True,
            'modified': datetime.now(),
        },
        {
            'sent': True,
            'content': 'Sure. What time were you thinking? I\'m about to attack Shredder now',
            'viewed': True,
            'modified': datetime.now(),
        },
        {
            'sent': False,
            'content': 'How about at 4pm?',
            'viewed': True,
            'modified': datetime.now(),
        },
    ],

    'Leonardo': [
        {
            'sent': False,
            'content': 'Hey there Donatello. Want to go out and get some pizza?',
            'viewed': True,
            'modified': datetime.now(),
        },
        {
            'sent': True,
            'content': 'Sure. What time were you thinking? I\'m about to attack Shredder now',
            'viewed': True,
            'modified': datetime.now(),
        },
        {
            'sent': False,
            'content': 'How about at 4pm?',
            'viewed': True,
            'modified': datetime.now(),
        },
    ]
}
