import mlflow.pyfunc

model_name = "Houses-Prices-Random-Forest"
stage = "Production"

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")



