from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

from messages.models import Message, MessageForm


def messages(request, thread_username=None):
    context = {}

    message = Message()

    threads = Message.objects.filter(
        recipient=request.user
    ).values_list(
        'sender__user',
        'sender__user__first_name',
        'sender__user__last_name'
    ).distinct()

    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        form.sender = request.user
        form.save()
    else:
        form = MessageForm(request.POST, instance=message)

    if thread_username is None and len(threads) > 0:
        first_message = Message.objects.filter(
            Q(recipient=request.user) | Q(sender=request.user)
        )[:1].get()

        current = first_message.recipient if first_message.sender == request.user else first_message.sender
    elif thread_username is not None:
        current = thread_username
    else:
        current = None

    messages = Message.objects.filter(
        Q(sender=current, recipient=request.user) |
        Q(sender=request.user, recipient=current)
    ).order_by(
        'created'
    )

    context['user'] = request.user
    context['message_form'] = form
    context['current_thread'] = current
    context['threads'] = threads
    context['messages'] = messages

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
