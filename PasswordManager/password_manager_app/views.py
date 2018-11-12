from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login

from .models import Entry
from .forms import UserForm

# Create your views here.


class EntryList(ListView):
    model = Entry
    template_name = 'entry_list.html'

    def get_context_data(self, **kwargs):
        if not self.request.user.is_anonymous:
            context = super().get_context_data(**kwargs)
            context['entries'] = Entry.objects.filter(user=self.request.user)
            context['logged_user'] = self.request.user
            return context


class EntryCreate(CreateView):
    model = Entry
    template_name = 'create.html'
    fields = ['site_name', 'site_url', 'login_name', 'login_password']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('password_manager:entries')


class EntryEdit(UpdateView):
    model = Entry
    template_name = 'details_and_edit.html'
    fields = ['site_name', 'site_url', 'login_name', 'login_password']
    success_url = reverse_lazy('password_manager:entries')


class EntryDelete(DeleteView):
    model = Entry
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('password_manager:entries')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('password_manager:entries')

        return render(request, self.template_name, {'form': form})
