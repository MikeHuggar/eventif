from django.contrib import admin
from django.db.models.signals import pre_save
from django.template.loader import render_to_string
from django.core import mail
from django.dispatch import receiver
from django.utils.timezone import now
from contact.models import Contact
from django.conf import settings


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message',
                    'created_at', 'reply', 'replied_at', 'is_replied')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'message', 'created_at', 'reply', 
                     'is_replied')
    list_filter = (['reply'])

    def replied_today(self, obj):
        return obj.replied_at.date() == now().date()

    replied_today.short_description = 'Respondido hoje?'
    replied_today.boolean = True

def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])

@receiver(pre_save, sender=Contact)
def mark_as_replied(sender, instance, **kwargs):
    if instance.reply != '' and instance.is_replied == False:
        instance.is_replied = True
        instance.replied_at = now()
        _send_mail(
            'contact/contact_reply.txt',
            vars(instance),
            'Mensagem respondida!',
            settings.DEFAULT_FROM_EMAIL,
            instance.email
        )


admin.site.register(Contact, ContactModelAdmin)