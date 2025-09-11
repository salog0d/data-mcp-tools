import boto3 

class S3Client:
    """
    Explicit auth to boto 3 instances
    """
    def __init__(self, client=None):
        self.client = client or boto3.client("s3")