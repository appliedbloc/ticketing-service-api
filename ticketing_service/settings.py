# Flask settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = '8888'
#FLASK_DEV_SERVER = '0.0.0.0:8888'
#FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = True


# Postgres
POSTGRES_URL = 'ticketdb.czt7kawu5hkq.us-east-1.rds.amazonaws.com:5432'
POSTGRES_USER = 'BAMF'
POSTGRES_PW = 'Appli3dbl0c!!'
POSTGRES_DB = 'ticketapi'
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False


