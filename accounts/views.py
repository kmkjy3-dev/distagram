from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/registration_success.html',{'new_user': user})
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})