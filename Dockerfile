
FROM python:3.10-alpine

WORKDIR /ia-agent

ENV FLASK_APP src/app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add g++
RUN apk add --no-cache zlib-dev gcc musl-dev jpeg-dev linux-headers freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev


COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install numpy
RUN pip3 install --no-cache-dir Pillow
RUN pip3 install jinja2
RUN pip3 install python_http_client
RUN pip3 install pyjwt
RUN pip3 install passlib[bcrypt]

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . /ia-agent