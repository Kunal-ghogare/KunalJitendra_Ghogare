from django.urls import path
from .views import Home, Add_Contact, Delete_Contact, Edit_Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_contact/', Add_Contact.as_view(), name= 'add_contact' ),
    path('delete_contact/', Delete_Contact.as_view(), name= 'delete_contact'),
    path('edit_contact/<int:id>/', Edit_Contact.as_view(), name='edit_contact')
    
]
