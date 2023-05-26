ARG PYTHON

FROM python:${PYTHON}-slim

RUN apt-get update && apt-get install -y pandoc

RUN curl -sSL https://install.python-poetry.org -o /tmp/install-poetry.py && \
    python /tmp/install-poetry.py && \
    rm -f /tmp/install-poetry.py && \
    poetry config virtualenvs.create false && \
    pip install -U pip

ADD poetry.lock /tmp
ADD pyproject.toml /tmp
RUN cd /tmp && poetry install

ADD docs/requirements.txt /tmp/requirements-docs.txt
RUN pip install -r /tmp/requirements-docs.txt

ADD . /ntc_rosetta

WORKDIR "/ntc_rosetta"

RUN poetry install
