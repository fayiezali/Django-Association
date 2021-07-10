from django.urls import path
#
# from django.contrib.auth import views as views_django_authentication # This Views Built-in Django
#
from accounts.views import *
# from .views import SignUpView 



urlpatterns = [
    path('my_login/'                 , My_Login.as_view()                  , name='My_Login_URL'),
    path('my_logout/'                , My_Logout.as_view()                 , name='My_Logout_URL'),
    path('my_logout_done/'           , My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
    path('my_signup/'                , My_Signup.as_view()                 , name='My_Signup_URL'),
    path('my_password_change/'       , My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
    path('my_password_change_done/'  , My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
    path('my_password_reset/'        , My_PasswordReset.as_view()          , name='My_PasswordReset_URL'),
    path('password_reset/done/'      , My_PasswordResetDone.as_view()      , name='My_PasswordResetDone_URL'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 
    
    
]