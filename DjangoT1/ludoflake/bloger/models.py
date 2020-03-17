from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Letter(models.Model):
    city = (
        ('MTL', 'Montreal'),
        ('LAV', 'Laval'),
        ('OTT', 'Ottawa'),
        ('TOK', 'Tokyo'),
        )
    penpal = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=10, choices=city)
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    sent_date = models.DateTimeField(blank=True, null=True)

    def send(self):
        # Link this to a button to set the send date
        self.sent_date = timezone.now()
        self.save()
    
    def valid_comment(self):
        # This will filter a list of comments and only show the ones that have
        # the atribut approved_comment=True
        return self.reviews.filter(validated_review=True)

    def get_absolute_url(self): # Function name needs to be get_absolute_url.
        return reverse("letter_detailed",kwargs={'pk':self.pk})
        # This sends the user to a destination when the letter is done.
    
    def __str__(self): #String representation of the model
        return self.location

class Review(models.Model):
    Letter = models.ForeignKey('bloger.Letter', related_name='reviews',
        on_delete=models.DO_NOTHING)
    reviewer = models.CharField(max_length=50)
    review_comment = models.TextField(max_length=150)
    stars = models.CharField(max_length=10, choices=((1,'one star'),(2,'two stars'),
    (3,'three stars'),(4,'four stars'),(5,'five stars')))
    creation_date = models.DateTimeField(default=timezone.now)
    validated_review = models.BooleanField(default=False)
    
    def validate(self):
        self.validated_review = True
        self.save()

    def get_absolute_url(self): # Function name needs to be get_absolute_url.
        return reverse("letter_list")

    def __str__(self):
        return self.review_comment