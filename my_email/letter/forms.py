from django import forms

class ComposeForm(forms.Form):
    recipient = forms.CharField(max_length=100, label='Получатель')
    subject = forms.CharField(max_length=200, label='Тема')
    body = forms.CharField(widget=forms.Textarea, label='Текст письма')