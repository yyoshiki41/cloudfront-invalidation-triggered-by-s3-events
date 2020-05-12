# cloudfront-invalidation-triggered-by-s3-events

Serverless: Create a CloudFront invalidation when S3 origin contents changed

## Motivation

Create an invalidation for a CloudFront distribution when S3 origin objects changed.

I need to filter origin objects by prefix and suffix.

## Design

1. Receive event notifications when S3 origin objects changed (`ObjectCreated`, `ObjectRemoved`)
2. Invoking AWS Lambda functions via Amazon S3 events
3. Create an invalidation for a CloudFront distribution to remove a file from CloudFront edge caches

## Resources

- S3 Bucket
- CloudFront Distribution
- Lambda (python3.8)

### Deploy a lambda function

```bash
$ DISTRIBUTION_ID=CF_DISTRIBUTION_ID \
S3_ORIGIN_BUCKET=YOUR_BUCKET_NAME \
PREFIX=hls \
SUFFIX=m3u8 \
serverless deploy
```

### Environment variables

- `S3_ORIGIN_BUCKET`
  S3 Bucket Name
- `DISTRIBUTION_ID`
  CloudFront distribution id
- `PREFIX`
  Configure notifications to be filtered by the prefix of the key name of objects
- `SUFFIX`
  Configure notifications to be filtered by the suffix of the key name of objects
