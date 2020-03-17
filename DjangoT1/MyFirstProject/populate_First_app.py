import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyFirstProject.settings')

import django

django.setup()

import random
from First_app.models import Bears, Webpage, AccessRecord, Users
from faker import Faker

fakegen = Faker()

bears = ['Jimmy', 'Rudy', 'Erwin', 'Falcon', 'Winston']

def add_bears ():
    b = Bears.objects.get_or_create(top_name=random.choice(bears))[0]
    b.save()
    return b

def populate(N=5):
    for entry in range (N):
        top = add_bears()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(Bears=top, url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

def populate2(N=4):
    for entry in range(N):
        F_Name=fakegen.first_name()
        L_Name=fakegen.last_name()
        Email=fakegen.email()
        Users.objects.get_or_create(First_name=F_Name, Last_name=L_Name,Email=Email)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(0)
    print('db was populated!')

    print('populating2 script!')
    populate2(4)
    print('db was populated2!')