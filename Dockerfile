FROM python:3.8 as build-python

RUN apt-get -y update

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

FROM python:3.8-slim

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

RUN groupadd -r quizzes && useradd -r -g quizzes quizzes

COPY . /app
COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
WORKDIR /app/quizzes

RUN SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input
RUN echo "\nDEBUG = False" > quizzes/custom_settings.py

RUN mkdir -p /app/quizzes/media /app/quizzes/static \
  && chown -R quizzes:quizzes /app/

EXPOSE 8000
ENV PORT 8000
ENV PYTHONUNBUFFERED 1
ENV PROCESSES 4

CMD ["quizzes/wsgi", ]
