from django.shortcuts import render
from .forms import PersonaForm
from django.shortcuts import render, redirect


def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = PersonaForm()

    return render(request, 'registro.html', {'forms': form})
