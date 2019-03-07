FROM python:3.7

USER root

COPY ./requirements.txt /app/requirements.txt
WORKDIR app

RUN /bin/bash -c "python3 -m venv venv \
    && source venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt"

COPY . /app
ENV FLASKAPP app
RUN chmod +x ./boot_app.sh
EXPOSE 5000
ENTRYPOINT ["./boot_app.sh"]
