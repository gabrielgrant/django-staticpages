import os

from django.http import Http404
from django.template import loader, TemplateDoesNotExist
from django.views.generic import TemplateView

class StaticpagesView(TemplateView):
    base_directory = ''
    def get_template_names(self):
        url_path = self.args[0].strip('/')
        if '..' in os.path.split(url_path):
            raise Http404
        dir_template = os.path.join(self.base_directory, url_path, 'index.html')
        page_template = os.path.join(self.base_directory, url_path + '.html')
        template_names = [dir_template, page_template]
        try:
            loader.select_template(template_names)
        except TemplateDoesNotExist:
            raise Http404
        return template_names
