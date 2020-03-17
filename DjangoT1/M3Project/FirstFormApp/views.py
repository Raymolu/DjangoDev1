from django.shortcuts import render
from . import forms
from django.core.exceptions import ValidationError

# Create your views here.


def initial(request):
    #return HttpResponse('<em>This is my second message<em>\n<h1>Header one</h1>\n<p style="color:red">This is a paragraph</p>')
    my_D = {'InsertPoint_1': 'Hey you !!!', 'InsertPoint_2': 'Can you see this?'}
    return render(request, 'FirstFormApp\initial.html', context=my_D)

def help(request):
    my_D = {'InsertPoint_1':'Bla bla bla this is the info to print'}
    return render(request, 'FirstFormApp\help.html', context=my_D)

def form_name_view(request):
    form = forms.FormName()
    print("Step1")

    if request.method == 'POST':
        print("Step2")

        form = forms.FormName(request.POST)

        if form.is_valid() and form.cleaned_data['botcatcher'] == '':
            print("Step3")

            print("Data validated")
            print("name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
        else:
            raise ValidationError("Bot typed: "+str(form.cleaned_data['botcatcher']))

    return render(request,'FirstFormApp/form1.html',{'form':form})

