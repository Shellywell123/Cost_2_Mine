#!/bin/bash

root="https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux"

if [[ $(uname -m) =~ "64" ]]; then
    echo "Fetching 64 bit geckodriver"
    url=$root"64.tar.gz"

elif [[ $(uname -m) =~ "armv7l" ]]; then
    echo "Fetching (old) ARM v7 geckodriver: consider compiling from source."
    url="https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz"
else
    echo "Fetching 32 bit geckodriver"
    url=$root"32.tar.gz"
fi

curl -L $url | tar xfz -
