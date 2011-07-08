import os
import shutil

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import TemplateView

rel_linksdir = os.path.join('staticpages', 'links')
abs_links_dir = os.path.join(os.path.dirname(__file__), 'templates', rel_linksdir)

def get_urls(sections=None):
    STATICPAGES_TEMPLATES = getattr(settings, 'STATICPAGES_TEMPLATES')
    if sections is not None and isinstance(sections, basestring):
        sections = [sections]
    if sections is None:
        sections = STATICPAGES_TEMPLATES
    else:
        sections = [section for section in STATICPAGES_TEMPLATES if section[0] in sections]
    urlpatterns = []
    if os.path.exists(abs_links_dir):
        shutil.rmtree(abs_links_dir)
    os.makedirs(abs_links_dir)
    for name, path in sections:
        os.symlink(path, os.path.join(abs_links_dir, name))
        for dirpath, dirnames, filenames in os.walk(path):
            dirpath_stripped = dirpath.strip('/') + '/'
            path_stripped = path.strip('/')
            reldir = dirpath_stripped[len(path_stripped):]
            for f in filenames:
                if f.endswith('.html'):
                    filepath = os.path.join(reldir.lstrip('/'), f)
                    urlpath = os.path.splitext(filepath)[0]
                    if f == 'index.html':
                        urlpath = urlpath[:-len('index')]
                        url_re = r'^%s$' % urlpath
                    else:
                        url_re = r'^%s/$' % urlpath
                    template_name = os.path.join(rel_linksdir, name, filepath)
                    view = TemplateView.as_view(template_name=template_name)
                    urlpattern = url_re, view
                    urlpatterns.append(urlpattern)
    return patterns('', *urlpatterns)

urlpatterns = get_urls()    
