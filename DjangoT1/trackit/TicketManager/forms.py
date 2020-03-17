from django import forms
from TicketManager.models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('company','contact', 'agent', 'text', 'status')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }