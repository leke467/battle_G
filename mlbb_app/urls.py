from django.urls import path, include

from mlbb_app import  views


urlpatterns = [

    path('mlbb/account/', views.Mlbb_Account_serializer_create.as_view(), name='mobile legends account'),
    path('mlbb/account/<int:mlbb_player_id>', views.mlbb_Account_update.as_view(), name='update mobile legends account'),
    path('mlbb/createsquad/', views.mlbbSquadCreate.as_view(), name='create mlbb squad'),
    path('mlbb/updatesquad/<int:pk>', views.mlbbSquadRetrieveUpdateDestroy.as_view(), name='update mlbb squad'),
    path('mlbb/squads/', views.mlbbSquadView.as_view(), name='all mlbb squad'),
    path('mlbb/squads/<int:squad_id>/invites/', views.SendSquadInviteView.as_view()),
    path('mlbb/squads/<int:squad_id>/invites/<int:invite_id>/', views.UpdateSquadInviteView.as_view()),
    path('mlbb/squads/<int:squad_id>/apply/', views.ApplyToSquadView.as_view()),
    path('mlbb/squads/<int:squad_id>/applications/<int:application_id>/', views.UpdateSquadApplicationView.as_view()),

]


