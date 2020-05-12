import json
import logging
import os
import time
import traceback

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CLOUDFRONT_DISTRIBUTION_ID = os.environ['CLOUDFRONT_DISTRIBUTION_ID']


def create_invalidation(path):
    cf = boto3.client('cloudfront')
    res = cf.create_invalidation(
        DistributionId=CLOUDFRONT_DISTRIBUTION_ID,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [path]
            },
            'CallerReference': str(time.time())
        })
    return res['Invalidation']['Id']


def lambda_handler(event, context):
    logger.info("START: Received event " + json.dumps(event))
    for items in event["Records"]:
        path = "/" + items["s3"]["object"]["key"]
    logger.info('Invalidate path is  %s', path)
    try:
        invalidation_id = create_invalidation(path)
        logger.info('COMPLETE: InvalidationId is %s', invalidation_id)
    except Exception as err:
        logger.error('EXCEPTION: %s', err)
        traceback.print_exc()
