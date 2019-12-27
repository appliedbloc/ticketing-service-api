from setuptools import setup, find_packages

setup(
    name='ticketing_service',
    version='1.0.0',
    description='Flask RestPlus powered ticketing service API',
    url='https://github.com/appliedbloc/ticketing-service-api.git',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rest restful api flask swagger flask-restplus',

    packages=find_packages(),

    install_requires=['flask-restplus==0.13.0', 'Flask-SQLAlchemy==2.4.1', 'pytest', 'sqlalchemy','psycopg2','uwsgi','gunicorn','flask-cors','requests']
)
