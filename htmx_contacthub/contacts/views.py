from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.db.models import Q
import time

@login_required
def index(request):
    contacts = request.user.contacts.all().order_by("-created_at")
    context = {'contacts': contacts}
    return render(request, 'contacts.html', context)

@login_required
def search_contacts(request):
    time.sleep(1)
    query = (request.GET.get('search', "")).strip()
    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    ).order_by("-created_at")
    return render(request, 'partials/contact-list.html', {"contacts": contacts})