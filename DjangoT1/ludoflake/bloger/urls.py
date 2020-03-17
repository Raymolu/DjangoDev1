from django.urls import path
from bloger import views

app_name = 'bloger'

urlpatterns = [
    path(r'', views.LetterListView.as_view(),name='letter_list'),
    path(r'letter/(<pk>\d+)', views.LetterDetailView.as_view(),name='letter_detailed'),
    path(r'letter/new/', views.CreateLetterView.as_view(),name='new_letter'),
    path(r'letter/(<pk>\d+)/update/', views.LetterUpdateView.as_view(),name='update_letter'),
    path(r'letter/(<pk>\d+)/delete/', views.LetterDeleteView.as_view(),name='delete_letter'),
    path(r'draft/', views.LetterDraftListView.as_view(),name='draft_letter_list'),
    path(r'info/', views.InfoOnView.as_view(),name='info'),
    path(r'letter/(<pk>\d+)/review/', views.add_review_to_post,name='add_review'),
    path(r'review/(<pk>\d+)/validate/', views.review_validation,name='review_validation'),
    path(r'review/(<pk>\d+)/dissmiss/', views.review_remove,name='review_dissmiss'),
    path(r'review/(<pk>\d+)/send/', views.letter_send,name='letter_send'),
    ]