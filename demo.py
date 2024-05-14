from dotenv import load_dotenv
import os
load_dotenv()

print(f"MLflow Tracking URI: {os.getenv('MLFLOW_TRACKING_URI')}")
print(f"MLFLOW TRACKING PASSWORD: {os.getenv('MLFLOW_TRACKING_PASSWORD')}")