FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN python setup.py develop
EXPOSE 8888

ENTRYPOINT python ticketing_service/app.py
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]