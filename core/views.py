from django.shortcuts import render
from django.views import View
from .models import Contact
from .forms import AddContactForm

class Home(View):
    def get(self, request):
        con_data = Contact.objects.all()
        return render(request, 'core/home.html',{'condata':con_data})
    
class Add_Contact(View):
    def get(self, request):
        fm = AddContactForm()
        return render(request, 'core/add_contact.html',{'form': fm})
