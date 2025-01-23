from constructs import Construct

from aws_cdk import Duration, aws_lambda as _lambda, aws_apigateway as apigateway

from .gateway_resource import GatewayResource
from .setup import ENVIRONMENT



class LambdaResource(Construct):
    
    def __init__(
        self,
        scope,
        construct_id: str,
        environment: ENVIRONMENT,
        gateway_resource: GatewayResource,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.gateway_resource = gateway_resource
        self.environment = environment.to_dict()
        
        # Creating layer
        self.layer = _lambda.LayerVersion(
            self,
            'Core_Layer',
            description='Layer with core dependencies',
            code=_lambda.Code.from_asset('lambda_layers'),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11]
        )
        
        self.root_resource = self.gateway_resource.root_resource
        
        
        # Create User
        self.create_user = self.__create_lambda_resource('create_user', 'POST')
        
    
    def __create_lambda(
        self,
        name: str,
        path: str = 'routes',
    ) -> _lambda.Function:
        return _lambda.Function(
            self,
            name.title(),
            handler=f'{name.lower()}.lambda_handler',
            code=_lambda.Code.from_asset(f'../app/{path}'),
            timeout=Duration.seconds(15),
            memory_size=512,
            environment=self.environment,
            runtime=_lambda.Runtime.PYTHON_3_11,
            layers=[self.layer]
        )
        
    def __create_lambda_resource(
        self,
        name: str,
        method: str,
        path: str = 'routes'
    ) -> _lambda.Function:
        lambda_function = self.__create_lambda(name, path)
        
        self.root_resource.add_resource(
        name.replace('_', '-'),
        default_cors_preflight_options=apigateway.CorsOptions(
            allow_origins=apigateway.Cors.ALL_ORIGINS,
            allow_methods=apigateway.Cors.ALL_METHODS,
            allow_headers=['*']
            )
        ).add_method(
            method,
            apigateway.LambdaIntegration(lambda_function),
            api_key_required=False
        )
        return lambda_function