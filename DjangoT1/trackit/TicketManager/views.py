from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView, FormView)
from TicketManager.models import Ticket

# Create your views here.
class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list_tp.html'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail_tp.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # print('--------------------> This is the data')
        # print(data['ticket'].company)
        # print('--------------------> Data end here')
        return data


class TicketFormView(FormView):
    model = Ticket
    template_name = 'ticket_form_tp.html'