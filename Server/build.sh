#!/bin/bash

docker buildx build --platform linux/amd64 -t kmu-fmcl/api:devel --load .
