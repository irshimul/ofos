from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserLoginForm, UserRegistrationForm
from .models import Customer


def logOut(request):
    logout(request)
    return render(request, 'user/logout.html')


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    # context_object_name =

    def get_queryset(self):
        return Customer.objects.all()


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'user/login.html'

    # display blank line
    def get(self, request):
        form = self.form_class(None)
        # print("get", form)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(username, password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('user:index')
        else:
            return HttpResponse("Not signed in")


class UserRegistrationFormView(View):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'

    # display blank line
    def get(self, request):
        form = self.form_class(None)
        # print("get", form)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):

        form = self.form_class(request.POST)

        user = form.save(commit=False)

        # cleaned (neutralized) data
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user.set_password(password)

        user.save()

        # returns user object if credentials are correct
        user = authenticate(request, first_name=first_name, last_name=last_name, username=username, password=password, email=email)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('user:index')

        return HttpResponse("Could not register")