FROM python:3.10-slim

COPY ../artifacts/1/08358ae11ea941c9af24ec914d38217e/artifacts/model/requirements.txt /requirements.txt
COPY ../data /data
COPY ../src /src
COPY ../requirements.txt /requirements2.txt
COPY ../artifacts/1/08358ae11ea941c9af24ec914d38217e/artifacts/model/model.pkl /model/model.pkl

RUN pip install -r requirements.txt && pip install -r requirements2.txt
#    conda clean -a


#SHELL ["conda", "run", "-n", "mlflow-env", "/bin/bash", "-c"]

ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

ENV BASIC_AUTH_USERNAME=$BASIC_AUTH_USERNAME_ARG
ENV BASIC_AUTH_PASSWORD=$BASIC_AUTH_PASSWORD_ARG

#ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "mlflow-env", "python", "src/main.py"]

#ENTRYPOINT ['mlflow', "models", "build-docker", "-m", "models:/Houses-Prices-Random-Forest/Production", "-n", "teste-mlops"]

ENTRYPOINT [ "python3" ]

CMD [ "src/main.py" ]