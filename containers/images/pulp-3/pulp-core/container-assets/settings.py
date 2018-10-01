# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
        'NAME': 'pulp',
        'USER': 'pulp',
        'CONN_MAX_AGE': 0,
    },
}

