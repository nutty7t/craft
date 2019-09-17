#!/usr/bin/env python3

import boto3
import json
import logging
import os
import sys
import tarfile

from botocore.exceptions import ClientError
from datetime import datetime


def create_backup(server_files_path: str):
    logging.info('Creating backup archive')
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    tarfile_name = f'{timestamp}.tar.gz'
    with tarfile.open(tarfile_name, 'w:gz') as tar:
        tar.add(server_files_path)
    return tarfile_name


def upload_backup(config: dict, space_name: str, backup_archive: str):
    try:
        logging.info('Uploading backup archive to DigitalOcean Spaces')
        session = boto3.session.Session()
        client = session.client('s3', **config)
        client.upload_file(
            backup_archive,
            space_name,
            backup_archive)
        logging.info('Success! \\( ﾟヮﾟ)/')
    except IOError:
        logging.error('Failed to open the archive file')
    except ClientError:
        logging.error('Failed to upload the backup archive')


def main():
    logging.basicConfig(
        datefmt='%m/%d/%Y %I:%M:%S %p',
        format='%(asctime)s :: %(levelname)s :: %(message)s',
        level=logging.INFO)
    try:
        space_config = {
            "region_name": os.environ['DIGITALOCEAN_SPACE_REGION'],
            "endpoint_url": os.environ['DIGITALOCEAN_SPACE_URL'],
            "aws_access_key_id": os.environ['DIGITALOCEAN_SPACE_KEY_ID'],
            "aws_secret_access_key": os.environ['DIGITALOCEAN_SPACE_SECRET']
        }
        space_name = os.environ['DIGITALOCEAN_SPACE_NAME']
        server_files = os.environ['MINECRAFT_SERVER_FILES']
    except KeyError:
        logging.error('One or more environment variables are not set.')
        sys.exit(1)

    backup = create_backup(server_files)
    upload_backup(space_config, space_name, backup)


if __name__ == '__main__':
    main()
