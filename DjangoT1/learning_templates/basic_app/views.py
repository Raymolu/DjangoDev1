from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hey you! is this it?','number':89}
    return render(request,'basic_app/index.html', context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
