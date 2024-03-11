FROM python:3.11.4-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR .

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /

RUN chmod +x ./prestart.sh
ENTRYPOINT ["./prestart.sh"]

