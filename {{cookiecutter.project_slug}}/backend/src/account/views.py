from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm

class UserSignUp(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Lógica para manejar un formulario válido, como crear un usuario
            return redirect('account:login')
        return render(request, 'registration/signup.html', {'form': form})