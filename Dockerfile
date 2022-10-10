FROM svizor/zoomcamp-model:3.9.12-slim


RUN pip install pipenv
COPY Pipfile .
RUN pipenv install
COPY main.py /app
COPY gunicorn_starter.sh /app 
WORKDIR /app
# RUN useradd lety && chown -R lety /app
# USER lety
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT ["./gunicorn_starter.sh"]