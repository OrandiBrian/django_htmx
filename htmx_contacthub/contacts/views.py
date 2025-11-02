from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.db.models import Q
from contacts.forms import ContactForm
import time
from django.views.decorators.http import require_http_methods

@login_required
def index(request):
    contacts = request.user.contacts.all().order_by("-created_at")
    context = {
        'contacts': contacts,
        'form': ContactForm()
        }
    return render(request, 'contacts.html', context)

@login_required
def search_contacts(request):
    time.sleep(1)
    query = (request.GET.get('search', "")).strip()
    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    ).order_by("-created_at")
    return render(request, 'partials/contact-list.html', {"contacts": contacts})

@login_required
@require_http_methods(["POST"])
def create_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save(commit=False) # don't save to the db yet
        contact.user = request.user
        contact.save()
        return render(request, 'partials/contact-row.html')
    else:
        form = ContactForm()
        
    return render(request, 'partials/contact-row.html', {'form': form})