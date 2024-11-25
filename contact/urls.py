from django.urls import path
from contact.views import showPage

app_name = 'contact'

urlpatterns = [
    path('', showPage, name='new'),
]