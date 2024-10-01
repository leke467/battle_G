from django.urls import path, include

from mlbb_app import  views


urlpatterns = [

    path('mlbb/account/', views.Mlbb_Account_serializer_create.as_view(), name='mobile legends account'),
    path('mlbb/account/<int:mlbb_player_id>', views.mlbb_Account_update.as_view(), name='update mobile legends account'),
    path('mlbb/createsquad/', views.Mlbb_squad_create.as_view(), name='create mlbb squad'),
    path('mlbb/updatesquad/<int:pk>', views.mlbb_squad_retrieve_update_destroy.as_view(), name='update mlbb squad'),
    path('mlbb/squads/', views.mlbb_squad_view.as_view(), name='all mlbb squad'),
    path('mlbb/squads/<int:squad_id>/invites/', views.Send_squad_invite_view.as_view()),
    path('mlbb/squads/<int:squad_id>/invites/<int:pk>/', views.Update_squad_invite_view.as_view()),
    path('mlbb/squads/<int:squad_id>/apply/', views.Apply_to_squad_view.as_view()),
    path('mlbb/squads/<int:squad_id>/applications/<int:pk>/', views.Update_squad_application_view.as_view()),
    path('mlbb/CreateCommunity/', views.Create_mlbb_community_view.as_view(), name='mlbb community'),
    path('mlbb/CommunityMembership/', views.Create_mlbb_community_membership_view.as_view(), name='mlbb community membership'),
    path('mlbb/community/<int:community_id>/', views.Update_mlbb_community_view.as_view(), name='update_mlbb community membership'),
    path('mlbb/community/', views.Mlbb_community_view.as_view(), name='view all mlbb community membership'),
    path('mlbb/community/<int:community_id>/apply/', views.Apply_to_community_view.as_view()),
    path('mlbb/community/<int:mlbb_community_id>/applications/<int:pk>/', views.Update_community_application_view.as_view()),

]


