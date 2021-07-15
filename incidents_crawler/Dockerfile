FROM python:3
WORKDIR /app

COPY conf.json .
COPY incidents_crawler.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt


CMD [ "python", "incidents_crawler.py" ]
