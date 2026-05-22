from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.is_active = False
            user.save()

            role = form.cleaned_data.get('role')

            group = Group.objects.get(name=role)

            user.groups.add(group)

            messages.success(
                request,
                'Account created successfully. Wait for admin approval.'
            )

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})
