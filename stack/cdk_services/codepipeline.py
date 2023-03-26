from dataclasses import dataclass, field
from constructs import Construct
from typing import Optional, List, Union
from aws_cdk.aws_codepipeline import CfnPipeline
from aws_cdk import CfnTag


@dataclass
class CodePipelineConfig:
    artifact_store: Optional[dict] = None
    disable_inbound_stage_transitions: Optional[List[dict]] = None
    name: Optional[str] = None
    restart_execution_on_update: Optional[bool] = None
    role_arn: Optional[str] = None
    stages: Optional[List[dict]] = None
    tags: Optional[List[CfnTag]] = None
    metadata: Optional[dict] = None

    def __post_init__(self) -> None:
        """
        Set default values for CodePipelineConfig parameters.

        :return: None
        """
        if not self.artifact_store:
            self.artifact_store = {"type": "S3", "location": "cdk-solutions-artifacts"}
        if not self.disable_inbound_stage_transitions:
            self.disable_inbound_stage_transitions = []
        if not self.name:
            self.name = "cdk-solutions-pipeline"
        if not self.restart_execution_on_update:
            self.restart_execution_on_update = True
        if not self.role_arn:
            self.role_arn = "arn:aws:iam::123456789012:role/cdk-solutions-role"
        if not self.stages:
            self.stages = []
        if not self.tags:
            self.tags = []
        if not self.metadata:
            self.metadata = {}


def create_codepipeline(
    scope: Construct, id: str, config: CodePipelineConfig
) -> CfnPipeline:
    """
    Create a CodePipeline using L1 constructs.

    :param scope: The AWS CDK Construct scope.
    :param id: The unique identifier of the CodePipeline Construct.
    :param config: An instance of CodePipelineConfig containing the configuration parameters.
    :return: The created CodePipeline instance.
    """
    return CfnPipeline(
        scope,
        id,
        artifact_store=config.artifact_store,
        disable_inbound_stage_transitions=config.disable_inbound_stage_transitions,
        name=config.name,
        restart_execution_on_update=config.restart_execution_on_update,
        role_arn=config.role_arn,
        stages=config.stages,
        tags=config.tags,
        metadata=config.metadata,
    )


def get_pipeline_stages(
    source_output: str,
    build_output: str,
    codecommit_repo: str,
    codebuild_project: str,
) -> List[dict]:
    """
    Generate the stages for a CodePipeline instance.

    :param source_output: The output artifact name for the source stage.
    :param build_output: The output artifact name for the build stage.
    :param codecommit_repo: The ARN of the CodeCommit repository.
    :param codebuild_project: The ARN of the CodeBuild project.
    :return: A list of dictionaries representing the stages.
    """
    return [
        {
            "name": "Source",
            "actions": [
                {
                    "name": "Source",
                    "actionTypeId": {
                        "category": "Source",
                        "owner": "AWS",
                        "provider": "CodeCommit",
                        "version": "1",
                    },
                    "outputArtifacts": [{"name": source_output}],
                    "configuration": {"RepositoryName": codecommit_repo},
                    "runOrder": 1,
                }
            ],
        },
        {
            "name": "Build",
            "actions": [
                {
                    "name": "Build",
                    "actionTypeId": {
                        "category": "Build",
                        "owner": "AWS",
                        "provider": "CodeBuild",
                        "version": "1",
                    },
                    "inputArtifacts": [{"name": source_output}],
                    "outputArtifacts": [{"name": build_output}],
                    "configuration": {"ProjectName": codebuild_project},
                    "runOrder": 1,
                }
            ],
        },
    ]
