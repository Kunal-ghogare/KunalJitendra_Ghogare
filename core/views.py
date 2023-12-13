from django.shortcuts import redirect, render
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
    
    def post(self, request):
        fm = AddContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add_contact.html',{'form': fm})
            
class Delete_Contact(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        condata = Contact.objects.get(id=id)
        condata.delete()
        return redirect('/')
    
    
class Edit_Contact(View):
    def get(self, request, id):
        con = Contact.objects.get(id=id)
        fm = AddContactForm(instance=con)
        return render(request, 'core/edit_contact.html', {'form':fm})
    
    def post(self,request,id):
        con = Contact.objects.get(id=id)
        fm = AddContactForm(request.POST, instance=con)
        if fm.is_valid():
            fm.save()
            return redirect('/')