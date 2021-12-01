SECRET_KEY = 'django-insecure-1^+0h#6ey$kgbnx15x6-i0of&=r=5=vv^aikjty2y@ls%zi_tb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'admin',
        'PASSWORD': '147258369zaq',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}