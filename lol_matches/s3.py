import os
import json
import boto3
from traceback import print_exc

from requests.models import Response

class S3Helper:
    def __init__(self, bucket, lol_region: str) -> None:
        self.client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('S3_SECRET_ACCESS_KEY'),
        )
        self.bucket = bucket
        self.s3_root = f'landing/{lol_region}'


    def save_dict(self, match_dict: dict, dataset: str, match_id: str):
        path = f'{self.s3_root}/{dataset}/{match_id}.json'
        match_json = json.dumps(match_dict)
        try:
            self.client.put_object(Body=match_json, Bucket=self.bucket, Key=path)
        except Exception:
            print_exc()


    def latest_dataset(self, dataset):
        list_params = {
            'Bucket': self.bucket,
            'Prefix': f'{self.s3_root}/{dataset}/'
        }
        try:
            paginator = self.client.get_paginator('list_objects')
            pages = paginator.paginate(**list_params)
            for page in pages:
                n_objects = len(page.get('Contents'))
                if n_objects < 1000:
                    last_page = page

            last_dataset = last_page.get('Contents')[-1].get('Key')
            last_dataset = last_dataset.split('/')[-1]
            last_dataset = last_dataset.split('.')[0]
        except Exception:
            print_exc()

        return int(last_dataset)
