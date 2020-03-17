from django.db import models

class Ticket(models.Model):
    '''
        Tracking ID
        Company
        Contact
        Agent
        Text
        Status
        StartDate
        EndDate
    '''
    companies = (('FirstWood', 'First Wood'), ('LumberExport', 'Lumber Export'),
                 ('JackInTheBox', 'Jack In The Box'), ('BigWood Inc.','Big Wood Inc.'), ('','other'))
    agents = (('Ludovic Raymond', 'Ludovic'), ('Jean Beauce', 'Jean'),
                 ('Tobby Love', 'Tobby'))
    status_options = (('open','Open'),('close','Close'),('stand_by','Stand by'))
    tracking_id = models.BigAutoField(primary_key=True)
    company = models.CharField(max_length=25, choices=companies)
    contact = models.CharField(max_length=25)
    agent = models.CharField(max_length=25, choices=agents)
    text = models.TextField()
    status = models.CharField(max_length=15, choices=status_options)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self): #String representation of the model
        return 'Ticket: ' + str(self.tracking_id)

    def get_absolute_url(self):
        return '/ticket/%i/' % self.tracking_id
