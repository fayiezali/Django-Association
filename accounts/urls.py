from django.urls import path
#
# from django.contrib.auth import views as views_django_authentication # This Views Built-in Django
#
from accounts.views import *
# from .views import SignUpView 



urlpatterns = [
    path('my_login/'                            , My_Login.as_view()                  , name='My_Login_URL'),
    path('my_logout/'                           , My_Logout.as_view()                 , name='My_Logout_URL'),
    path('my_logout_done/'                      , My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
    #**********************************************************************************************************************
    path('my_signup/'                           , My_Signup.as_view()                 , name='My_Signup_URL'),
    path('my_profile_update/<int:pk>/'          , My_ProfileUpdate.as_view()          , name='my_profile_update_URL'),
    path('my_Profile_delete/<int:pk>/delete/'   , My_ProfileDelete.as_view()          , name='my_Profile_delete_URL'),
    path('my_profile_list/'                     , my_profile_list.as_view()           , name='my_profile_list_URL'),
    # path('my_profile_detail_slug/<slug:slug>/'  , My_Profile_Detail_Slug.as_view()    , name='My_Profile_Detail_Slug_URL'), 
    #**********************************************************************************************************************
    path('my_Profile_Detail_ID/<int:pk>/'       , My_Profile_Detail_ID.as_view()      , name='My_Profile_Detail_ID_URL'),
    # path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
    # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
    # *****************************************

    
    path('my_password_change/'                 , My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
    path('my_password_change_done/'            , My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
    path('my_password_reset/'                  , My_PasswordReset.as_view()          , name='My_PasswordReset_URL'),
    path('password_reset/done/'                , My_PasswordResetDone.as_view()      , name='My_PasswordResetDone_URL'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 
    
    
]