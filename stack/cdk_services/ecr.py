from dataclasses import dataclass, field, asdict
from typing import Optional, List
from constructs import Construct
from aws_cdk.aws_ecr import CfnRepository
from enum import Enum, auto


class AutoNameEnum(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self

    def __str__(self):
        return self.name


class EncryptionType(AutoNameEnum):
    AES256 = auto()
    KMS = auto()


class ImageTagMutability(AutoNameEnum):
    MUTABLE = auto()
    IMMUTABLE = auto()


class ImageScanOnPush(AutoNameEnum):
    ENABLED = auto()
    DISABLED = auto()


@dataclass
class EncryptionConfiguration:
    encryption_type: EncryptionType = EncryptionType.AES256
    kms_key_id: Optional[str] = None


@dataclass
class ImageScanningConfiguration:
    scan_on_push: ImageScanOnPush = ImageScanOnPush.DISABLED


@dataclass
class CfnRepositoryProps:
    repository_name: Optional[str] = None
    encryption_configuration: Optional[
        EncryptionConfiguration
    ] = EncryptionConfiguration(encryption_type=EncryptionType.AES256)
    image_scanning_configuration: Optional[
        ImageScanningConfiguration
    ] = ImageScanningConfiguration(scan_on_push=ImageScanOnPush.ENABLED)
    image_tag_mutability: ImageTagMutability = ImageTagMutability.MUTABLE
    tags: Optional[List[dict]] = field(default_factory=list)
    encryption_configuration = EncryptionConfiguration(
        encryption_type=EncryptionType.AES256
    )
    lifecycle_policy = {
        "rules": [
            {
                "rulePriority": 1,
                "description": "Expire images older than 30 days",
                "selection": {
                    "tagStatus": "untagged",
                    "countType": "sinceImagePushed",
                    "countUnit": "days",
                    "countNumber": 30,
                },
                "action": {"type": "expire"},
            }
        ]
    }


def create_ecr_repository(
    scope: Construct, id: str, config: CfnRepositoryProps
) -> CfnRepository:
    """
    Create an ECR repository using L1 constructs.

    :param scope: The AWS CDK Construct scope.
    :param id: The unique identifier of the ECR repository Construct.
    :param config: An instance of EcrRepositoryConfig containing the configuration parameters.
    :return: The created ECR repository instance.
    """
    if config.encryption_configuration and config.encryption_configuration.kms_key_id:
        config.encryption_configuration.kms_key_id = str(
            config.encryption_configuration.kms_key_id
        )
    return CfnRepository(scope, id, **asdict(config))
