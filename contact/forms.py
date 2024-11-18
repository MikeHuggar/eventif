from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome")
    email = forms.EmailField(label="E-Mail")
    phone = forms.CharField(label="Telefone")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)