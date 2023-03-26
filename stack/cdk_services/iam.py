from dataclasses import asdict, dataclass
from typing import List

from aws_cdk import aws_iam as iam
from aws_cdk import Stack


@dataclass
class IAMRoleConfig:
    role_name: str
    assumed_by_service: str
    policies: List[str] = None
    description: str = None
    max_session_duration: int = None


def create_iam_role(stack: Stack, id: str, config: IAMRoleConfig) -> None:
    role = iam.Role(self, "Role",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        description="Example role..."
    )
    lambda_role = iam.Role(self, "Role",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        description="Example role..."
    )
    
    stream = kinesis.Stream(self, "MyEncryptedStream",
        encryption=kinesis.StreamEncryption.KMS
    )
    
    # give lambda permissions to read stream
    stream.grant_read(lambda_role)
    principal = iam.ServicePrincipal(service=config.assumed_by_service)
    cfn_role = iam.CfnRole(self, "MyCfnRole",
        assume_role_policy_document=assume_role_policy_document,
    
        # the properties below are optional
        description="description",
        managed_policy_arns=["managedPolicyArns"],
        max_session_duration=123,
        path="path",
        permissions_boundary="permissionsBoundary",
        policies=[iam.CfnRole.PolicyProperty(
            policy_document=policy_document,
            policy_name="policyName"
        )],
        role_name="roleName",
        tags=[CfnTag(
            key="key",
            value="value"
        )]
    )

    role = iam.CfnRole(
        stack,
        id,
        **asdict(config),
    )
