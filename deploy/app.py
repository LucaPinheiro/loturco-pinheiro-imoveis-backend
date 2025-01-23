#!/usr/bin/env python3
import os

import aws_cdk as cdk

from deploy.deploy.setup import ENVIRONMENT
from deploy.deploy_stack import DeployStack


app = cdk.App()
DeployStack(app, "DeployStack",
    app,
    env=cdk.Environment(
        account=ENVIRONMENT.AWS_ACCOUNT_ID,
        region=ENVIRONMENT.AWS_REGION
    ),
    environment=ENVIRONMENT
)

app.synth()
