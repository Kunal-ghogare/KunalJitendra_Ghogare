from django.urls import path
from .views import Home, Add_Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_contact/', Add_Contact.as_view(), name= 'add_contact' )
]
