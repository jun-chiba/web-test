#!/bin/bash

aws s3 sync --exact-timestamps --delete ./src s3://chiba-test-app
