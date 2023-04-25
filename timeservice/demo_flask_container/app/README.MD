Description
Folder: demo_flask_container
description:  This flask based REST API will be deployed inside a container and deployed in lambda and 
the API gateway will be hosted by AWS API gateway.

Function/endpoints:
1. "/getisraeltime/<str:us_unix_timestamp>" - will return the equivalent working hour in Israel based on the us timezone.


Requirements:
1. python 3.8
2. python3-pip
3. Git
4. ECR repository details. (e.g. number, name, and "push commands". )
5. Flask *
6. Zappa *
7. flask_restful *
8. pipenv
9. awscli (amazon web service command line interface)
10. AWS access and secret key.  Please refer to IAM security credentials and make sure the user has programmatic access and able to use services.
    1. run command: "aws configure" and enter the keys and values for storing credentials in the session.

note: for the sake of brevity, i didnt use flask[async] as i think the performance of sync with async will not be big.

* (please refer to requirements.txt for the version)

Files:
1. zappa_settings.json - zappa settings file.  Can be generated using zappa init.
   1. !important: please specify s3_bucket.
2. app.py - flask app.
3. requirements.txt - dependencies the application requires to run in the container.
4. Dockerfile - docker file to deploy the flask within the container


Instruction.
1. Navigate to demo_flask_container/app/ directory.
Building the container and pushing to the repository. 
Run following command:
2. "zappa save-python-settings-file container_lambda_flask" - will generate the python file for zappa_settings.json
3. "docker build -t container-lambda-flask:latest ." - docker will build and tag the "Dockerfile" image.
4. go to your ECR and open the "push commands" for the container.  Follow the instruction for pushing the repository.
   1. aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ######.dkr.ecr.us-east-1.amazonaws.com
      1. login the aws credential.  Make sure you have the access key and secret key configured in this session.
   2. docker build -t <image name> .    (e.g.  docker build -t demo-container-lambda .)
      1. Build container
   3. docker tag demo-lambda-flask:latest ########.dkr.ecr.us-east-1.amazonaws.com/demo-container-lambda:latest
      1. Tag the container before pushing in ECR
   4. docker push ######.dkr.ecr.us-east-1.amazonaws.com/demo-container-lambda:latest
      1. Push container to ECR.
Deploying using Zappa
5. run command: "zappa deploy container_lambda_flask" -d xxxxx.dkr.ecr.us-east-1.amazonaws.com/demo-container-lambda:latest"
   1. deploy the container using cloudformation.  Zappa will configure create a lambda function and reference the container in ECR.  API gateway will then create and deploy an API.
   2. after deployment, your URI will be provided which you will use for deploying your "working hour service"
6. If you have changes in your codes, just run again the following codes.
   1. zappa save-python-settings-files container_lambda_flask
   2. docker build -t container-lambda-flask:latest .
   3. docker tag. please refer to  3.3
   4. docker push. please refer to  4.1
   5. zappa update lambda  container_lambda_flask" -d xxxxx.dkr.ecr.us-east-1.amazonaws.com/demo-container-lambda:latest

