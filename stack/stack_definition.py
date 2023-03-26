from aws_cdk import Stack, aws_ecr, aws_ecs, aws_ecs_patterns
from aws_cdk.aws_ecr_assets import DockerImageAsset
from constructs import Construct


class GoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.docker_image = DockerImageAsset(
            self,
            "GoDockerImage",
            directory="./stack",
        )
        # Create a new Fargate task definition
        # task_definition = ecs.FargateTaskDefinition(self, 'MyTaskDefinition',
        #                                             memory_limit_mib=512,
        #                                             cpu=256)

        # # Add a new container to the task definition using the Docker image from the ECR repository
        # container = task_definition.add_container('MyContainer',
        #                                            image=ecs.ContainerImage.from_ecr_repository(image_asset.repository),
        #                                            ...)

        # # Configure auto scaling for the task definition
        # auto_scaling = ecs.FargateService(self, 'MyFargateService',
        #                                   task_definition=task_definition,
        #                                   desired_count=1,
        #                                   max_healthy_percent=200,
        #                                   min_healthy_percent=50)