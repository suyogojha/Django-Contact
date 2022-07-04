from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Contact


# Create your views here.

#def home(request):
#    return render(request, "index.html", {'contacts': Contact.objects.all()})


#def detail(request, pk):
#    context = {
#        'contact': get_object_or_404(Contact, pk=pk)
#    }
#    return render(request, "detail.html", context)

class ContactDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "contact"
    model = Contact
    template_name = "detail.html"


class HomeListView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = Contact
    context_object_name = "contacts"

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)

class ContactCreateView(LoginRequiredMixin ,CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Your contact has been successfully created')
        return redirect("app:home")


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = "/"

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Your contact has been updated successfully!")
        return redirect("app:detail", instance.pk)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "delete.html"
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your contact has been successfully deleted!')
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("app:home")

@login_required
def search(request):
    if request.GET:
        search_term = request.GET.get('search_term')
        contacts = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term)
        ).filter(manager=request.user)
        return render(request, "search.html", {'contacts': contacts, 'search_term': search_term})
    redirect("app:home")
