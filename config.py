import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


import os
# from urllib.parse import quote_plus

# password = quote_plus('root')
# DATABASE_URL = f"mysql://root:{password}@localhost/blogpost"

DATABASE_URL = f"mysql://root:root@localhost/blogpost"



class Config:
    
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_never_guess'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    POSTS_PER_PAGE = 3
    
    # MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    # MAIL_PORT = 2525 or 25
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = '548d1c28eb2b66'
    # MAIL_PASSWORD = '9928c8a32454cf'
    # ADMINS = ['sujitsanap1111@gmail.com']
    
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'sujitsanap143@gmail.com'
    MAIL_PASSWORD = 'gied vrga ehhl dhbe'
    ADMINS = ['sujitsanap143@gmail.com']
    
    
    LANGUAGES = ['en', 'hi']
    
    ELASTICSEARCH_URL = 'http://localhost:9200'
    