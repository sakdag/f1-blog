from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from apps.communities.models import Community, CommunityMember


class CreateCommunity(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Community


class SingleCommunity(DetailView):
    model = Community


class ListCommunities(ListView):
    model = Community


class JoinCommunity(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('communities:single_community', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        community = get_object_or_404(Community, slug=self.kwargs.get('slug'))

        try:
            CommunityMember.objects.create(user=self.request.user, community=community)
        except IntegrityError:
            messages.warning(self.request, 'You are already a member!')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)


class LeaveCommunity(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('communities:single_community', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = CommunityMember.objects.filter(
                user=self.request.user,
                community__slug=self.kwargs.get('slug')
            ).get()
        except IntegrityError:
            messages.warning(self.request, 'Community Member does not exist!')
        else:
            membership.delete()
            messages.success(self.request, 'You have successfully left the community!')

        return super().get(request, *args, **kwargs)
