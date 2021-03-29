from django.shortcuts import render, redirect
from  django.views.generic import CreateView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from .forms import SignUpForm, UserProfileForm
from .models import UserAccount


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.add_message(request, messages.INFO, 'You successfully signed up!')
            return redirect('create_profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', locals())


class NewProfileView(CreateView, LoginRequiredMixin):
    model = UserAccount
    template_name = 'create_profile.html'
    form_class = UserProfileForm
    context_object_name = 'new_profile'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        messages.add_message(request, messages.INFO, 'You successfully create your profile!')
        return redirect('profile')


class MyProfileView(View, LoginRequiredMixin):
    def get(self, request):
        p = request.user.profile
        return render(request, 'profile.html', locals())


@login_required
def update_profile(request, pk):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'You successfully update your profile!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'update_profile.html', locals())





