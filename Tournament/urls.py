from django.urls import path
from Tournament import views

urlpatterns = [
    path('create_tournament/', views.Create_Tournament_view.as_view(), name='create_tournament'),
    path('tournament_participants/', views.Tournament_participants_view.as_view(), name='tournament_participants'),
    path('all_tournaments/', views.All_tournaments_view.as_view(), name='all-tournaments'),
    path('edit-tournament-detail/<int:tournament_id>/', views.Edit_tournament_detail.as_view(), name='edit_tournament_detail'),
    path('edit-participants/<int:participant_id>/', views.Edit_tournament_participants_detail.as_view(), name='edit-participants-detail'),
    path('create_bracket/', views.Bracket_view.as_view(), name='create_bracket'  ),
    path('update_bracket/<int:bracket_id>/', views.Bracket_update_view.as_view(), name='update_bracket' ),
    path('match/', views.Match_view.as_view(), name='create_match'),
    path('update_match/<int:id>/', views.Match_update_view.as_view(), name='update_match')

]