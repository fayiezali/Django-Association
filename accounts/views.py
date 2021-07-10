
from django.conf import settings
#
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
#
# from django.contrib.auth.decorators import login_required
#
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm , PasswordResetForm, SetPasswordForm,
)
#
from django.contrib.auth.views import LoginView , LogoutView , TemplateView , PasswordChangeView , PasswordResetView
#
from django.utils import timezone
#
from django.views import generic
#
from django.views.generic import CreateView 
#
from accounts.forms import SignUpForm
#
from django.urls import reverse_lazy
#
#
#
#
#
#
# Log In The System
class My_Login(LoginView):
    template_name = 'registration/my_login.html'  # The Page HTML to Display
    #
    #
    # extra_context = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() # Data To Be Sent
        return context # Send This Data To The Required Page HTML

#
#
#
#
#
#
# Log Out Of The System:
class My_Logout(LogoutView):
    template_name = 'registration/my_logout.html'
#
#
#
#
#
#
# Display Them About Page
class My_LogoutDone(TemplateView):
    template_name = 'registration/my_logout_done.html' # The Page HTML to Display
#
#
#
#
#
#
# Registration New User
class My_Signup(CreateView):
    # form_class = UserCreationForm # This Registration Form From Django
    form_class = SignUpForm # This Registration Form From (accounts/forms.py)
    template_name = 'registration/my_signup.html'# User Registration Page HTML
    success_url = reverse_lazy('IndexHomeTemplateView-URL') # Go To In This Page After Registration
#
#
#
#
#
#
class My_PasswordChange(PasswordChangeView):
    template_name = 'registration/my_password_change.html' 
    success_url = reverse_lazy('My_PasswordChangeDone_URL')
#
# 
#
#
#
#
class My_PasswordChangeDone(TemplateView):
    template_name = 'registration/my_password_change_done.html'
    title = ('password change successful')


from urllib.parse import urlparse, urlunparse

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView

UserModel = get_user_model()

class My_PasswordReset(PasswordResetView):
    email_template_name = 'registration/my_password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('My_PasswordResetDone_URL')
    template_name = 'registration/my_password_reset.html'
    title = _('Password reset')
    token_generator = default_token_generator


INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class My_PasswordResetDone(TemplateView):
    template_name = 'registration/my_password_reset_done.html'
    title = _('Password reset sent')


# class PasswordResetConfirmView(PasswordContextMixin, FormView):
#     form_class = SetPasswordForm
#     post_reset_login = False
#     post_reset_login_backend = None
#     reset_url_token = 'set-password'
#     success_url = reverse_lazy('password_reset_complete')
#     template_name = 'registration/password_reset_confirm.html'
#     title = _('Enter new password')
#     token_generator = default_token_generator

#     @method_decorator(sensitive_post_parameters())
#     @method_decorator(never_cache)
#     def dispatch(self, *args, **kwargs):
#         assert 'uidb64' in kwargs and 'token' in kwargs

#         self.validlink = False
#         self.user = self.get_user(kwargs['uidb64'])

#         if self.user is not None:
#             token = kwargs['token']
#             if token == self.reset_url_token:
#                 session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
#                 if self.token_generator.check_token(self.user, session_token):
#                     # If the token is valid, display the password reset form.
#                     self.validlink = True
#                     return super().dispatch(*args, **kwargs)
#             else:
#                 if self.token_generator.check_token(self.user, token):
#                     # Store the token in the session and redirect to the
#                     # password reset form at a URL without the token. That
#                     # avoids the possibility of leaking the token in the
#                     # HTTP Referer header.
#                     self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
#                     redirect_url = self.request.path.replace(token, self.reset_url_token)
#                     return HttpResponseRedirect(redirect_url)

#         # Display the "Password reset unsuccessful" page.
#         return self.render_to_response(self.get_context_data())

#     def get_user(self, uidb64):
#         try:
#             # urlsafe_base64_decode() decodes to bytestring
#             uid = urlsafe_base64_decode(uidb64).decode()
#             user = UserModel._default_manager.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist, ValidationError):
#             user = None
#         return user

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.user
#         return kwargs

#     def form_valid(self, form):
#         user = form.save()
#         del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
#         if self.post_reset_login:
#             auth_login(self.request, user, self.post_reset_login_backend)
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.validlink:
#             context['validlink'] = True
#         else:
#             context.update({
#                 'form': None,
#                 'title': _('Password reset unsuccessful'),
#                 'validlink': False,
#             })
#         return context


# class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
#     template_name = 'registration/password_reset_complete.html'
#     title = _('Password reset complete')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['login_url'] = resolve_url(settings.LOGIN_URL)
#         return context


# class PasswordChangeView(PasswordContextMixin, FormView):
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('password_change_done')
#     template_name = 'registration/password_change_form.html'
#     title = _('Password change')

#     @method_decorator(sensitive_post_parameters())
#     @method_decorator(csrf_protect)
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs

#     def form_valid(self, form):
#         form.save()
#         # Updating the password logs out all other sessions for the user
#         # except the current one.
#         update_session_auth_hash(self.request, form.user)
#         return super().form_valid(form)


# class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
#     template_name = 'registration/password_change_done.html'
#     title = _('Password change successful')

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)































































# from django.shortcuts import render
# #
# # This Is Built-in Django
# from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# #
# from django.contrib.auth import REDIRECT_FIELD_NAME, login
# #
# from django.utils.decorators import method_decorator
# #
# from django.urls import reverse_lazy
# #
# from django.views import generic
# #
# from django.views.generic import CreateView 
# #
# from accounts.forms import SignUpForm
#
#
#
#
#
#
# Registration New User
# class SignUpView(CreateView):
#     # form_class = UserCreationForm # This Registration Form From Django
#     form_class = SignUpForm # This Registration Form From Django
#     success_url = reverse_lazy('login') # Go To In This Page After Registration
#     template_name = 'registration/signup.html'# User Registration Page HTML
#
#
#
#
#
#
# class LoginView(FormView):
#     form_class = AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#     success_url=  reverse_lazy('index_home.html')

