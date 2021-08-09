from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from apps.communities.models import Community


class CreateCommunity(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Community


class SingleCommunity(DetailView):
    model = Community


class ListCommunities(ListView):
    model = Community
