from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict
from aws_cdk.aws_codebuild import CfnProject
from constructs import Construct


@dataclass
class CodeBuildProjectConfig:
    name: str
    artifacts: dict
    environment: dict
    source: dict
    badge_enabled: Optional[bool] = None
    cache: Optional[dict] = None
    description: Optional[str] = None
    encryption_key: Optional[str] = None
    file_system_locations: Optional[List[dict]] = None
    logs_config: Optional[dict] = None
    queued_timeout: Optional[int] = None
    secondary_artifacts: Optional[List[dict]] = None
    secondary_sources: Optional[List[dict]] = None
    secondary_source_versions: Optional[List[dict]] = None
    service_role: Optional[str] = None
    source_version: Optional[str] = None
    tags: Optional[List[Dict[str, str]]] = None
    timeout: Optional[int] = None
    vpc_config: Optional[dict] = None


def create_codebuild_project(
    scope: Construct, id: str, config: CodeBuildProjectConfig
) -> CfnProject:
    """
        Create a CodeBuild Project using L1 constructs.
    W
        :param scope: The AWS CDK Construct scope.
        :param id: The unique identifier of the CodeBuild Project Construct.
        :param config: An instance of CodeBuildProjectConfig containing the configuration parameters.
        :return: The created CodeBuild Project instance.
    """
    return CfnProject(scope, id, **asdict(config))
