DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "Mmg6YjVqZ0c2MVRJOVUuMlR1a2ExQklKelVxNGc0V3JBYXIySTdNWmxicTYucXBTWGI1YXkyTTJiVFF1UHprNDNlZWVXSnNZcDRPTURJc3pZayxjejluZ1lRdV9OR3E3LFNTN0JINU5CM2xHZ0dqckFGWHh5Rjg2eERjNTRwZHc="
