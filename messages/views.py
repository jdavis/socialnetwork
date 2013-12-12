from datetime import datetime

from django.shortcuts import render


def messages(request):
    context = {}
    context['messages'] = dummy_data

    return render(request, 'messages/index.html', context)

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
