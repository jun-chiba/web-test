#!/bin/bash
pwd
aws s3 sync --exact-timestamps --delete /webapp s3://chiba-test-app
