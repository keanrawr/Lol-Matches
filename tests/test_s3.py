import os
from lol_matches.s3 import S3Helper

region = 'europe'
bucket_name = os.getenv('S3_BUCKET_NAME')
s3 = S3Helper(bucket_name, region)


# Test is too expensive if number of saved matches gets large enough
# def test_last_match():
#     last = s3.latest_dataset('match')
#     assert isinstance(last, int)
