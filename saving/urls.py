from django.urls import path

from . import views

from saving.views import AssociationCreateView , AssociationListView , AssociationDetailViewSlug , AssociationDetailViewID , AssociationUpdateView , AssociationDeleteView

urlpatterns = [
    # ...
    path('association/add/'                    , AssociationCreateView.as_view()     , name='AssociationCreateView-add-URL'),
    path('associationlist/'                    , AssociationListView.as_view()       , name='AssociationListView-list-URL'),
    path('associationdetailslug/<slug:slug>/'  , AssociationDetailViewSlug.as_view() , name='AssociationDetailViewSlug-detail-URL'), 
    # *****************************************
    path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationDetailViewID-detail-URL'),
    path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
    # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
    # *****************************************
    path('associationupdate/<int:pk>/'         , AssociationUpdateView.as_view()     , name='AssociationUpdateView-update-URL'),
    path('associationdelete/<int:pk>/delete/'  , AssociationDeleteView.as_view()     , name='AssociationDeleteView-delete-URL'),


]