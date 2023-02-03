FROM python

WORKDIR ./app

RUN pip install redis

COPY . .

CMD [ "python", "app.py" ]