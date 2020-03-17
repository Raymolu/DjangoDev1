from django.shortcuts import render
from django.http import HttpResponse
from First_app.models import Bears, Webpage, AccessRecord, Users

# Create your views here.


def index(request):
    #return HttpResponse('<em>This is my second message<em>\n<h1>Header one</h1>\n<p style="color:red">This is a paragraph</p>')
    my_D = {'insert_me': 'Hey you !!!', 'insert_me2': 'Can you see this?'}
    webpages_list = AccessRecord.objects.order_by('date')
    usernames_list = Users.objects.order_by('Last_name')
    main_dict = {'access_records':webpages_list, 'Users':usernames_list}
    return render(request, 'First_app\index.html', context=main_dict)
    # return render(request, 'First_app\index.html', context=my_D), render(request, 'First_app\index.html', context=date_dict)

def help(request):
    my_D = {'helpme':'Bla bla bla this is the info to print'}
    return render(request, 'First_app\help.html', context=my_D)