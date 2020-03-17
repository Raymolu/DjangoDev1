from bloger.models import Letter, Review
from bloger.forms import LetterForm, ReviewForm

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

@login_required
def letter_send(request,pk):
    letter = get_object_or_404(letter, pk=pk)
    letter.send()
    return redirect('letter_detailed',pk=pk)    

# Create your views here.
class InfoOnView(TemplateView):
    template_name = 'info.html'

class LetterListView(ListView):
    model = Letter
    template_name = 'letter_list.html'
    def get_queryset(self):
        return Letter.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date')

class LetterDetailView(DetailView):
    model = Letter

class CreateLetterView(LoginRequiredMixin, CreateView):
    login_url = '/login/' # required for the mixin
    redirect_field_name = 'bloger/letter_detail.html' # required for the mixin
    form_class = LetterForm
    model = Letter

class LetterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/' # required for the mixin
    redirect_field_name = 'bloger/letter_detail.html' # required for the mixin
    form_class = LetterForm
    model = Letter

class LetterDeleteView(LoginRequiredMixin, DeleteView):
    model = Letter
    success_url = reverse_lazy('bloger:letter_list')

class LetterDraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/' # required for the mixin
    redirect_field_name = 'bloger/letter_detail.html' # required for the mixin
    form_class = LetterForm
    model = Letter
    def get_queryset(self):
        return Letter.objects.filter(sent_date__isnull=Ture).order_by('creation_date')

#-----------------------------------------------------------------------------------------------

@login_required
def add_review_to_post (request, pk):
    letter = get_object_or_404(Letter, pk=pk)
    if request.method == 'LETTER':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.letter = letter
            review.save()
            return redirect ('letter_detailed',pk=letter.pk)
    else:
        form = ReviewForm()
    return render(request, 'letter/review_form.html', {'form':form})

@login_required
def review_validation(request, pk):
    review = get_object_or_404(review, pk=pk)
    review.validate()
    return redirect('letter_detailed',pk=review.letter.pk)

@login_required
def review_remove(request, pk):
    review = get_object_or_404(review, pk=pk)
    letter_pk = review.letter.pk
    review.delete()
    return redirect('letter_detailed',pk=letter_pk)