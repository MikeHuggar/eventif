from django.db import models


class Contact(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20, blank=True)
    message = models.TextField('mensagem', max_length=600)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    reply = models.TextField('resposta', max_length=600, blank=True)
    replied_at = models.DateTimeField('respondido em', blank=True, null=True)
    is_replied = models.BooleanField('respondido', default=False)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name