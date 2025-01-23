from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from .gateway_resource import GatewayResource
from .lambda_resource import LambdaResource

class DeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, environment, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        gateway_resource = GatewayResource(
            self,
            construct_id=environment.STACK_NAME + "_Gateway",
            environment=environment
        )
        
        lambda_resource = LambdaResource(
            self,
            construct_id=environment.STACK_NAME + "_Lambda", 
            gateway_resource=gateway_resource,
            environment=environment,
        )