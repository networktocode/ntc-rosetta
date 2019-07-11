#!/bin/bash
set -e

PLUGIN_DIR=`/usr/bin/env python -c 'import openconfig_pyang; import os; print ("{}/plugins".format(os.path.dirname(openconfig_pyang.__file__)))'`

cd ..
rm -f docs/models/dynamic/*
for i in $(find models/* -maxdepth 1 -type d); do
    model=`basename $i`
    make build-model-doc MODEL=$model OC_PYANG_PLUGINS_DIR=$PLUGIN_DIR
done
