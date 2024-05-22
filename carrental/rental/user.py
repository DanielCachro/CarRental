from django.shortcuts import render
from . import forms

def login(request):
    return render(request, 'login.html.jinja')

def logout(request):
    return render(request, 'logout.html.jinja')

def register(request):
   if request.method == 'POST':
        form_user = forms.RegistrationForm(request.POST)
        form_address = forms.UserAddressFormSet(request.POST)
        if form_user.is_valid() and form_address.is_valid():
                user = form_user.save()
                addresses = form_address.save(commit=False)
                for address in addresses:
                    address.user = user
                    address.save()
                return render(request, 'register.html.jinja', {'message': 'Success'})
        return render(request, 'register.html.jinja', {'message': 'Coś nie poszło'})
   else:
        form_user = forms.RegistrationForm()
        form_address = forms.UserAddressFormSet()
        return render(request, 'register.html.jinja', {'form_user': form_user, 'form_address': form_address})
    




# def register(request):
#     if request.method == 'POST':
#         user_form = forms.RegistrationForm(request.POST)
#         address_formset = forms.UserAddressFormSet(request.POST)
#         if user_form.is_valid() and address_formset.is_valid():
#             # Zapisz użytkownika
#             user = user_form.save()
#             # Zapisz adresy użytkownika
#             addresses = address_formset.save(commit=False)
#             for address in addresses:
#                 address.user = user