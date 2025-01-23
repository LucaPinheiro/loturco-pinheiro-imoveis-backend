import datetime
from typing import Any, Dict
from aws_cdk import (
    Duration,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct

from .setup import ENVIRONMENT


class GatewayResource(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, environment: ENVIRONMENT, **kwargs: Dict[str, Any]) -> None:
        super().__init__(scope, construct_id)
        
        # Creating the API Gateway Rest API
        self.api_gateway = apigateway.RestApi(
            self,
            'Loturco_Pinheiro_Gateway',
            rest_api_name='LoturcoPinheiroImoveisAPI',
            description='API para o sistema de imóveis da Loturco Pinheiro',
            default_cors_preflight_options=apigateway.CorsOptions(
            allow_origins=apigateway.Cors.ALL_ORIGINS,
            allow_methods=apigateway.Cors.ALL_METHODS,
            allow_headers=['*']
            ),
            deploy_options=apigateway.StageOptions(
            stage_name=environment.STAGE
            )
        )
        
        # Creating deployment
        self.deployment = apigateway.Deployment(
            self, 
            f'Deployment{int(datetime.datetime.now().timestamp())}',
            api=self.api_gateway
        )
        
        # Creating root resource 
        self.root_resource = self.api_gateway.root.add_resource('properties', default_cors_preflight_options={
            "allow_origins": apigateway.Cors.ALL_ORIGINS,
            "allow_methods": apigateway.Cors.ALL_METHODS,
            "allow_headers": ['*']
        })
        