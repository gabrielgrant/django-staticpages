import os

from django.conf.urls.defaults import patterns, url
from django.conf import settings
from django.views.generic import TemplateView

from .views import StaticpagesView

def make_pattern(name, base_url, d):
    parts = [base_url.strip(os.path.sep), '(.*?)/?$']
    re = '^' + '/'.join(p for p in parts if p)
    return url(re,
        StaticpagesView.as_view(base_directory=d), name=name)

STATICPAGES_TEMPLATES = getattr(settings, 'STATICPAGES_TEMPLATES', [])
# reorder to not eclipse the longer, more specific, regexes
STATICPAGES_TEMPLATES.sort(key=lambda x: (-len(x[1].split('/')), -len(x[1])))

urlpatterns = patterns('',
    *[make_pattern(name, base_url, base_dir) for name, base_url, base_dir in STATICPAGES_TEMPLATES]
)
