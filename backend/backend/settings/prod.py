from .common import *

# DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

STATICFILES_STORAGE = "backend.storages.StaticAzureStorage"
DEFAULT_FILE_STORAGE = "backend.storages.MediaAzureStorage"

# AZURE_ACCOUNT_NAME = os.environ["AZURE_ACCOUNT_NAME"]
# AZURE_ACCOUNT_KEY = os.environ["AZURE_ACCOUNT_KEY"]
AZURE_ACCOUNT_NAME = 'demodaystorage'
AZURE_ACCOUNT_KEY = 'kfycL+iOXqJvqAydRi96IgGK+/63FTAMEJEC3SId86tkjfzQJquuIMpJConp0A1JJSU31QutJEj8+ASt1G7agQ=='