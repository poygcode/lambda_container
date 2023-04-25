Description
Folder: demo_flask_no_container
description:  This flask based REST API will be deployed in lambda and the API gateway will be hosted by AWS API gateway.

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
8. virtualenv 
9. awscli (amazon web service command line interface)
10. AWS access and secret key.  Please refer to IAM security credentials and make sure the user has programmatic access and able to use services.
    1. run command: "aws configure" and enter the keys and values for storing credentials in the session.

* (please refer to requirements.txt for the version)

Files:
1. zappa_settings.json - zappa settings file.  Can be generated using zappa init.
   1. !important: please specify s3_bucket.
2. app.py - flask app.
3. requirements.txt - dependencies the application requires to run in the container.

Instruction.
1. Navigate to demo_flask_no_container/app/ directory.
2. run command: virtualenv venv
   1. create virtual environment first.
3. run command: pip install -r requirements.txt
   1. install dependencies.
4. run command: zappa deploy dev
5. Zappa will then create a deployment script to be launch in api gateway.
6. to update, run command: zappa update dev
   1. note: dev is the name of the stage in the zappa_settings.json
