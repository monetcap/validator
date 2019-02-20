#!/usr/bin/env bash
docker build -t monetcap/validator:experimental .

docker run --rm -v $(pwd)/out:/tmp/out -v $(pwd)/sample.xlsx:/tmp/sample.xlsx monetcap/validator:experimental -xfp /tmp/sample.xlsx
