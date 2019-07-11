FROM python:3.6

RUN pip install \
    pytest \
    yangson \
    -e git://github.com/dbarrosop/oc-pyang.git@ntc-yang-models#egg=oc-pyang \
    sphinx \
    sphinx_rtd_theme

WORKDIR /ntc-yang-models
