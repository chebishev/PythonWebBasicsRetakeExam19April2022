from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam19April2022.game_app.forms import GameForm


# Create your views here.
def game_delete(request):
    return None


def game_create(request):
    form = GameForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'game_app/create-game.html', {'form': form})


def game_details(request):
    return None


def game_edit(request):
    return None
