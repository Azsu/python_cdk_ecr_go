from aws_cdk import core
from constructs import Construct
from ecr import create_ecr_repository, ECRRepositoryConfig
from codepipeline import create_codepipeline, CodePipelineConfig, get_pipeline_stages
from codebuild import create_codebuild_project, CodeBuildProjectConfig
from codecommit import create_codecommit_repository, CodeCommitRepoConfig
from s3 import create_s3_bucket, S3BucketConfig


class MyCdkStack(core.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ECR Repository
        ecr_config = ECRRepositoryConfig(repository_name="my-ecr-repo")
        create_ecr_repository(self, "ECRRepo", ecr_config)

        # CodePipeline
        pipeline_config = CodePipelineConfig(
            artifact_store={"type": "S3"},
            role_arn="arn:aws:iam::123456789012:role/service-role/codepipeline-role",
            stages=get_pipeline_stages(),
        )
        create_codepipeline(self, "CodePipeline", pipeline_config)

        # CodeBuild
        codebuild_config = CodeBuildProjectConfig(
            artifacts={"type": "CODEPIPELINE"},
            environment={"build_image": "aws/codebuild/standard:5.0"},
            source={"type": "CODEPIPELINE", "build_spec": "buildspec.yml"},
            service_role="arn:aws:iam::123456789012:role/service-role/codebuild-role",
        )
        create_codebuild_project(self, "CodeBuildProject", codebuild_config)

        # CodeCommit Repository
        codecommit_config = CodeCommitRepoConfig(
            repository_name="my-codecommit-repo"
        )
        create_codecommit_repository(self, "CodeCommitRepo", codecommit_config)

        # S3 Bucket
        s3_config = S3BucketConfig()
        create_s3_bucket(self, "S3Bucket", s3_config)
