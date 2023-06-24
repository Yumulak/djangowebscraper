import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from JobScrappy.forms import ScheduleScrapesForm
from JobScrappy.models import Users
from django.views.generic import ListView
from JobScrappy import sendemail



def home(request):
    return render(
        request,
        'JobScrappy/home.html'
    )

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Users

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def submitsuccess(request):
    form = ScheduleScrapesForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            url = form.cleaned_data["urllist"]
            email = form.cleaned_data["email"]
            interval = form.cleaned_data["interval"]
            user = form.save(commit=False)
            user.log_date = datetime.now()
            user.save()
            Users.__str__(user)
            sendemail.scrape_job_ads(url)
            sendemail.send_email(email, url, interval)
            return redirect('home')
    else:      
        return render(
            request,
            'JobScrappy/submitsuccess.html',
            {'form': form})