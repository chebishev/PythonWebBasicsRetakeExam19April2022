from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam19April2022.profile_app.forms import CreateProfileForm


# Create your views here.
def profile_create(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home page')

    return render(request, 'profile_app/create-profile.html', {'form': form})


def profile_details(request):
    return None


def profile_edit(request):
    return None


def profile_delete(request):
    return None
