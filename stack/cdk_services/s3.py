from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict
from aws_cdk.aws_s3 import CfnBucket
from constructs import Construct


from dataclasses import dataclass
from typing import Optional


@dataclass
class S3BucketConfig:
    scope: Optional["Construct"] = None
    id: Optional[str] = None
    accelerate_configuration: Optional[dict] = {"accelerationStatus": "Suspended"}
    access_control: Optional[str] = "Private"
    analytics_configurations: Optional[list] = []
    bucket_encryption: Optional[dict] = {
        "serverSideEncryptionConfiguration": [
            {"applyServerSideEncryptionByDefault": {"sseAlgorithm": "AES256"}}
        ]
    }
    bucket_name: Optional[str] = None
    cors_configuration: Optional[list] = []
    intelligent_tiering_configurations: Optional[list] = []
    inventory_configurations: Optional[list] = []
    lifecycle_configuration: Optional[dict] = {
        "rules": [
            {
                "id": "DeleteOldObjects",
                "status": "Enabled",
                "prefix": "",
                "expiration": {"days": 30},
                "noncurrentVersionExpirationInDays": 30,
            }
        ]
    }
    logging_configuration: Optional[dict] = None
    metrics_configurations: Optional[list] = []
    notification_configuration: Optional[dict] = None
    object_lock_configuration: Optional[dict] = None
    object_lock_enabled: Optional[bool] = None
    ownership_controls: Optional[dict] = None
    public_access_block_configuration: Optional[dict] = {
        "blockPublicAcls": True,
        "blockPublicPolicy": True,
        "ignorePublicAcls": True,
        "restrictPublicBuckets": True,
    }
    replication_configuration: Optional[dict] = None
    tags: Optional[list] = None
    versioning_configuration: Optional[dict] = {"status": "Suspended"}
    website_configuration: Optional[dict] = None


def create_s3_bucket(scope: Construct, id: str, config: S3BucketConfig) -> CfnBucket:
    """
    Create an S3 Bucket using L1 constructs.

    :param scope: The AWS CDK Construct scope.
    :param id: The unique identifier of the S3 Bucket Construct.
    :param config: An instance of S3BucketConfig containing the configuration parameters.
    :return: The created S3 Bucket instance.
    """
    return CfnBucket(scope, id, **asdict(config))
