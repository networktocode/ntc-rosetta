ARG PYTHON

FROM python:${PYTHON}-bullseye

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y pandoc openssl && \
    apt-get autoremove -y && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/* && \
    pip --no-cache-dir install --upgrade pip wheel

RUN curl -sSL https://install.python-poetry.org -o /tmp/install-poetry.py && \
    python /tmp/install-poetry.py && \
    rm -f /tmp/install-poetry.py

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false

ADD poetry.lock /tmp
ADD pyproject.toml /tmp
RUN cd /tmp && poetry install

ADD docs/requirements.txt /tmp/requirements-docs.txt
RUN pip install -r /tmp/requirements-docs.txt

ADD . /ntc_rosetta

WORKDIR "/ntc_rosetta"

RUN poetry install
