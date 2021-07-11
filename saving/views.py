from django.shortcuts import render
#
from django.views.generic import TemplateView , ListView ,DetailView , CreateView, DeleteView, UpdateView
#
from django.urls import reverse_lazy
#
# Only a Logged In User can call this view
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
#
"""
# The current user's permissions are stored in a template variable called {{ perms }}
# LoginRequiredMixin:
    Only a Logged In User Can Call This (Views)
# PermissionRequiredMixin:
    You Can check whether the Current User Has particular Permission
    Using variable Name {{ perms}} Within django "app"
"""
#
from saving.models import AssociationData_MODEL
#
from django.utils import timezone
#
#
#
#
#
#













# Display The Home Page
class IndexHomeTemplateView(TemplateView):
    template_name = "index_home.html" # The Page HTML to Display
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Number Of visits To The Site:
        # Get a Session Value Setting a Default If It Is Not Present.
        num_visits = self.request.session.get('num_visits', 1)
        # Render the HTML template index.html with the data in the context variable.
        context['number_of_visits_site'] =self.request.session['num_visits'] = num_visits+1 
        return context # Send This Data To The Required Page HTML
#
#
#
#
#
#
# Display Them About Page
class AboutTemplateView(TemplateView):
    template_name = "about.html" # The Page HTML to Display
#
#
#
#
#
#
# Create New Record
class AssociationCreateView(LoginRequiredMixin , CreateView):
    model = AssociationData_MODEL # Data Table
    fields = ['ASS_NameAssociation', # Fields Table
                'ASS_Slug', 
                'ASS_AssociationLogo', 
                'ASS_Address',
                'ASS_Mobile', 
                'ASS_Phone', 
                'ASS_Email',
                'ASS_BankAccount',
                ]
    success_url = reverse_lazy('AssociationListView-list-URL') # Go To In This Page After Add/Create New
#
#
#
#
#
#
# Display List Record
class AssociationListView(LoginRequiredMixin , ListView):
    model = AssociationData_MODEL # Data Table
    paginate_by = 4  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() # Data To Be Sent
        return context # Send This Data To The Required Page HTML
        
# class AssociationListView(LoginRequiredMixin , ListView):
#     """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
#     model = AssociationData_MODEL
#     template_name = 'saving/associationdata_model_list.html'
#     paginate_by = 5
#
#
#
#
#
#
# Display Detail Record By: Slug
class AssociationDetailViewSlug(LoginRequiredMixin ,  DetailView):
    model = AssociationData_MODEL # Data Table
    slug_field = 'ASS_Slug' # Filter Field Use 'Slug'
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
## Display Detail Record By: ID
class AssociationDetailViewID(LoginRequiredMixin , DetailView):
    model = AssociationData_MODEL # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() # Data To Be Sent
        return context # Send this Data to the Required page HTML
#
#
#
#
#
#
# Update Record.
class AssociationUpdateView(LoginRequiredMixin , UpdateView):
    model = AssociationData_MODEL # Data Table
    fields = ['ASS_NameAssociation', # Fields Table
                'ASS_Slug', 
                'ASS_AssociationLogo', 
                'ASS_Address',
                'ASS_Mobile', 
                'ASS_Phone', 
                'ASS_Email',
                'ASS_BankAccount',
                ]
    success_url = reverse_lazy('AssociationListView-list-URL') # Go To In This Page After Add/Create New
#
#
#
#
#
#
# Delete Record.
class AssociationDeleteView(LoginRequiredMixin  , DeleteView):
    model = AssociationData_MODEL # Data Table
    success_url = reverse_lazy('AssociationListView-list-URL') # Go To In This Page After Add/Create New
#
#
#
#
#
#