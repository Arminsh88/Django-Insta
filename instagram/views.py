from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def home(request):
    # rc_url = reverse('profile', kwargs={'username': 'Armin'})
    # return HttpResponseRedirect(rc_url)
    return redirect('user_manager:login')