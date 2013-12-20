from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect

from profiles.models import UserProfile
from messages.models import Message, MessageForm


def messages(request, user_id=None):
    context = {}

    message = Message()

    threads = Message.objects.filter(
        recipient=request.user
    ).values_list(
        'sender__user',
        'sender__user__first_name',
        'sender__user__last_name'
    ).distinct()

    if user_id is None and len(threads) > 0:
        first_message = Message.objects.filter(
            Q(recipient=request.user) | Q(sender=request.user)
        )[:1].get()

        current = first_message.recipient if first_message.sender == request.user else first_message.sender
    elif user_id is not None:
        current = user_id
    else:
        current = None

    if request.method == 'POST':
        message.sender = request.user.get_profile()
        message.recipient = UserProfile.objects.get(user__pk=user_id)

        form = MessageForm(request.POST, instance=message)
        form.save()

        return redirect('/messages/' + user_id)
    else:
        form = MessageForm(request.POST, instance=message)


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


def new_message(request, user_id=None):
    context = {}

    message = Message()
    recipient = UserProfile.objects.get(user__pk=user_id)

    if request.method == 'POST':
        message.sender = request.user.get_profile()
        message.recipient = recipient

        form = MessageForm(request.POST, instance=message)
        form.save()

        return redirect('/messages/' + user_id)
    else:
        form = MessageForm(request.POST, instance=message)

    context['user'] = request.user
    context['recipient'] = recipient
    context['form'] = form

    return render(request, 'messages/new.html', context)
