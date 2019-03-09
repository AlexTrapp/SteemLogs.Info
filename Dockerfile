# This is a copy of Python 3.6's onbuild script (python:3.6-onbuild)
# https://raw.githubusercontent.com/docker-library/python/7eca63adca38729424a9bab957f006f5caad870f/3.6/onbuild/Dockerfile
# Cannot use 3.6-onbuild directly due to pip compatibility issues with steem-python.
FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
# Downgrade pip due to compatibility issues with steem-python
RUN pip install pip==9.0.3 && pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app


