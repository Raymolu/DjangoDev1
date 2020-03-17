from django import forms
from bloger.models import Letter, Review

class LetterForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = ('penpal','location', 'content',)

        widgets = {
            'location': forms.MultipleChoiceField(),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('reviewer', 'review_comment', 'stars',)

        widgets = {
            'reviewer': forms.TextInput(attrs={'class': 'textinputclass'}),
            'review_comment': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
