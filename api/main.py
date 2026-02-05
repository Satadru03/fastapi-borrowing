from fastapi import FastAPI
import joblib
import pandas as pd
import logging
import time

from schema import Borrower
app = FastAPI()

logging.basicConfig(
    filename="../logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Load model once at startup
model = joblib.load("model.pkl")

logger.info("Model loaded successfully")

@app.post("/predict")
def predict(borrower: Borrower):
    start_time = time.time()

    try:
        input_data = borrower.model_dump(mode="json")
        logger.info(f"Request received: {input_data}")

        data = pd.DataFrame([input_data])
        prediction = model.predict(data)[0]
        probability = float(model.predict_proba(data)[0][1])

        if int(prediction) > 0.45:
            decision = "will_default"
        else:
            decision = "will_not_default"

        response = {
            "Default": int(prediction),
            "decision": {decision},
            "probability": round(probability, 3)
        }

        duration = time.time() - start_time
        logger.info(f"Response sent: {response} | Time: {duration:.4f}s")

        return response

    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            f"Prediction failed | Input: {borrower.model_dump(mode="json")} | "
            f"Error: {str(e)} | Time: {duration:.4f}s"
        )

        return {
            "error": "Prediction failed",
            "detail": str(e)
        }
