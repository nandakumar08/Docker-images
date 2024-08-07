#!/bin/bash

# Variables
REPO_URL="https://github.com/nandakumar08/Docker-images.git"
BRANCH="master"
BUCKET_NAME="nandaproject"
TEMP_DIR="repo"

# Clean up any existing directory
rm -rf $TEMP_DIR

# Download the repository
git clone --branch $BRANCH $REPO_URL $TEMP_DIR

# Upload files to S3
aws s3 sync $TEMP_DIR s3://$BUCKET_NAME

# Clean up
rm -rf $TEMP_DIR
