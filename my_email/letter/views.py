from django.shortcuts import render, redirect, get_object_or_404
from .models import Letter
from .forms import ComposeForm

def compose_view(request):
    if request.method == 'POST':
        form = ComposeForm(request.POST)
        
        if form.is_valid():
            to_user = form.cleaned_data['recipient']
            topic = form.cleaned_data['subject']
            text = form.cleaned_data['body']

            
            new_message = Letter.objects.create(
                sender='student@university.ru',
                recipient=to_user,
                subject=topic,
                body=text,
                folder='outbox' 
            )
            new_message.save() 

            return redirect('outbox')
    else:
        form = ComposeForm()

    return render(request, 'letter/compose.html', {'form': form})


def inbox_view(request):
    messages = Letter.objects.filter(folder='inbox')
    return render(request, 'letter/list.html', {'messages': messages, 'current_folder': 'Входящие'})


def outbox_view(request):
    messages = Letter.objects.filter(folder='outbox')
    return render(request, 'letter/list.html', {'messages': messages, 'current_folder': 'Исходящие'})


def archive_view(request):
    messages = Letter.objects.filter(folder='archive')
    return render(request, 'letter/list.html', {'messages': messages, 'current_folder': 'Архив'})


def trash_view(request):
    messages = Letter.objects.filter(folder='trash')
    return render(request, 'letter/list.html', {'messages': messages, 'current_folder': 'Корзина'})


def detail_view(request, message_id):
    message = get_object_or_404(Letter, id=message_id)

    if message.is_read == False:
        message.is_read = True
        message.save()

    return render(request, 'letter/detail.html', {'message': message})


def move_view(request, message_id, new_folder):
    message = get_object_or_404(Letter, id=message_id)
    message.folder = new_folder
    message.save()
    return redirect('inbox')


def delete_view(request, message_id):
    message = get_object_or_404(Letter, id=message_id)
    message.delete()
    return redirect('inbox')