from django.shortcuts import render
from website.models import *
from django.contrib.auth.decorators import login_required
from .tools import *
from django.http import Http404


# Definition of views:

def index(request):
    context = {}
    home_header = get_website_section('home_header')
    getting_started = get_website_section('getting_started')
    latest_news = get_latest_news_posts(5)
    highlighted_publications = Publication.objects.filter(is_highlighted=True)

    context['home_header'] = home_header
    context['getting_started'] = getting_started
    context['latest_news'] = latest_news
    context['highlighted_publications'] = highlighted_publications

    context['gplus_feed'] = get_google_plus_activity("107763702707848478173",
                                                     4)
    context['fb_posts'] = get_facebook_page_feed("diffusionimaginginpython", 5)
    context['tweets'] = get_twitter_feed('dipymri', 5)

    return render(request, 'website/index.html', context)


def page(request, position_id):
    context = {}
    try:
        section = get_website_section(position_id)
    except:
        raise Http404("Page does not exist")

    context['section'] = section
    return render(request, 'website/section_page.html', context)


def cite(request):
    context = {}
    all_publications = Publication.objects.all()
    context['all_publications'] = all_publications
    return render(request, 'website/cite.html', context)


def honeycomb(request):
    context = {}
    all_honeycomb_posts = HoneycombPost.objects.all()
    context['all_honeycomb_posts'] = all_honeycomb_posts
    return render(request, 'website/honeycomb.html', context)


def support(request):
    return render(request, 'website/support.html', {})


@login_required
def dashboard(request):
    return render(request, 'website/dashboard.html', {})


def dashboard_login(request):
    next_url = request.GET.get('next')
    return render(request, 'website/dashboard_login.html', {'next': next_url})
