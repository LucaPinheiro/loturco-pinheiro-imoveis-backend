from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from deploy.deploy.gateway_resource import GatewayResource
from deploy.deploy.lambda_resource import LambdaResource

class DeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, environment, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        gateway_resource = GatewayResource(
            self,
            construct_id='Loturco_Pinheiro_Gateway',
            environment=environment
        )
        
        lambda_resource = LambdaResource(
            self, 
            gateway_resource=gateway_resource,
            environment=environment,
        )