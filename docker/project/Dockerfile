FROM python:3.8

WORKDIR /usr/src/app

COPY docker/project/ /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y && apt-get install \
    postgresql \
    gcc \
    python3-dev \
    musl-dev -y \
    postgresql \
    postgresql-contrib \
    && apt install mc -y
RUN pip install --upgrade pip


RUN pip install -r requirements.txt

# COPY ./Docker/project/entrypoint.sh .
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
