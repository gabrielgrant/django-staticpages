# from http://www.travisswicegood.com/2010/01/17/django-virtualenv-pip-and-fabric/

from django.conf import settings
from django.core.management import call_command

# put the app name here
app_to_test = 'staticpages'

def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            app_to_test,
            '%s.tests' % app_to_test,
        ),
        # Django replaces this, but it still wants it. *shrugs*
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/tmp/django_login.db',
            }
        },
        MEDIA_ROOT = '/tmp/django_login_test_media/',
        ROOT_URLCONF = '',
        DEBUG = True,
		TEMPLATE_DEBUG = True,
    ) 
    
    #call_command('syncdb')
    
    # Fire off the tests
    call_command('test', app_to_test)
    

if __name__ == '__main__':
    main()

