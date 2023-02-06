FROM python:3.10.9-alpine3.16

WORKDIR /usr/src/app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache bash
    
RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY . .
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]