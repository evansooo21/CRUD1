from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from dashboard.forms import Register, UserEditForm, ProfileEditForm
from dashboard.models import Profile


class UserRegisterView(CreateView):
    form_class = Register
    template_name = 'registration/register.html'
    success_url = reverse_lazy('regcomp')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.save()
            return render(request, 'register_done.html', {'new_user': new_user})


def Reg_comp(request):
    return render(request, 'register_done.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request,'dashboard.html', {'section': 'dashboard'})



@login_required
def edit(request):
    if request.method == "POST":
        user_form= UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error uploading your profile')
    else:
        user_form= UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'edit.html', {'user_form':user_form, 'profile_form':profile_form})