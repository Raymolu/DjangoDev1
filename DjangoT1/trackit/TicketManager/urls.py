from django.conf.urls import url
from django.urls import path
from TicketManager import views

app_name = 'TicketManager_URL' # Name to use relative names from this urls.py file

urlpatterns = [
    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('detail/<int:pk>', views.TicketDetailView.as_view(), name='ticket_detail'),
    # path('form/', views.TicketFormView.as_view(), name='ticket_form'),
]