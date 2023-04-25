FROM amazon/aws-lambda-python:3.8

#ARG FUNCTION_DIR="/var/task/"

COPY ./ ${LAMBDA_TASK_ROOT}

RUN pip install pipenv && pipenv install
RUN pip install -r requirements.txt

# generate handler for lambda.
RUN ZAPPA_HANDLER_PATH=$( \
    python -c "from zappa import handler; print (handler.__file__)" \
    ) \
    && echo $ZAPPA_HANDLER_PATH \
    && cp $ZAPPA_HANDLER_PATH ${LAMBDA_TASK_ROOT}

CMD [ "handler.lambda_handler" ]