from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict
from aws_cdk.aws_codeartifact import CfnRepository
from constructs import Construct


@dataclass
class CodeCommitRepoConfig:
    repository_name: Optional[str] = None
    triggers: Optional[List[dict]] = None
    code: Optional[dict] = None
    repository_description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


def create_codecommit_repository(
    scope: Construct, id: str, config: CodeCommitRepoConfig
) -> CfnRepository:
    """
    Create a CodeCommit Repository using L1 constructs.

    :param scope: The AWS CDK Construct scope.
    :param id: The unique identifier of the CodeCommit Repository Construct.
    :param config: An instance of CodeCommitRepoConfig containing the configuration parameters.
    :return: CodeCommit Repository resource.
    """
    return CfnRepository(scope, id, **asdict(config))
