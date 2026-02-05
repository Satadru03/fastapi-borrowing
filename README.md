# Loan Default Predictor API

A production-ready **machine learning inference API** that predicts whether a loan applicant is likely to **default**, along with the model’s confidence score.

The project demonstrates an **end-to-end ML system**:
data → model → FastAPI → Docker → documented API.

---

## 🚀 What Problem This Solves

Loan providers need a **quick, consistent, and explainable** way to assess credit risk.

This API:

* Takes structured borrower information
* Predicts whether the borrower is likely to **default**
* Returns both:

  * a **binary prediction**
  * a **probability score** (risk confidence)

The API is designed to be:

* reproducible
* deployable
* easy to integrate into backend systems

---

## 🧠 Model Output Explained

The response contains two key fields:

### `Default`

* `1` → borrower is predicted to **default**
* `0` → borrower is predicted to **not default**

This classification uses the **0.45 probability threshold**.

---

### `probability`

* A float between `0` and `1`
* Represents the model’s confidence that the borrower will default

Example:

```json
"probability": 0.72
```

Means:

> “The model estimates a 72% chance of default.”

Returning probability allows **risk thresholds to be adjusted later** without retraining the model.

---

## 🛠️ How to Run (Docker – 2 Minutes)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Satadru03/fastapi-borrowing.git
cd loan-default-api
```

---

### 2️⃣ Build the Docker image

```bash
docker build -t loan-default-api .
```

---

### 3️⃣ Run the container

```bash
docker run -p 8000:8000 loan-default-api
```

---

### 4️⃣ Open API docs

Open in browser:

```
http://localhost:8000/docs
```

Interactive Swagger UI is available.

---

## 📡 API Endpoint

### `POST /predict`

Accepts borrower information and returns a default prediction.

---

## ✅ Example – Normal Input (Low Risk)

### Request

```json
{
  "Age": 35,
  "Income": 60000,
  "LoanAmount": 12000,
  "CreditScore": 720,
  "MonthsEmployed": 48,
  "NumCreditLines": 3,
  "InterestRate": 8,
  "LoanTerm": 36,
  "DTIRatio": 0.25,
  "Education": "Bachelor's",
  "EmploymentType": "Full-time",
  "MaritalStatus": "Married",
  "LoanPurpose": "Auto",
  "HasMortgage": "No",
  "HasDependents": "No",
  "HasCoSigner": "No"
}
```

### Response

```json
{
  "Default": 0,
  "decision": "will_not_default",
  "probability": 0.345
}
```

---

## ⚠️ Example – Edge Case (High Risk)

Young borrower with minimal income and poor credit history.

### Request

```json
{
  "Age": 18,
  "Income": 10000,
  "LoanAmount": 1000,
  "CreditScore": 300,
  "MonthsEmployed": 0,
  "NumCreditLines": 1,
  "InterestRate": 2,
  "LoanTerm": 12,
  "DTIRatio": 0.1,
  "Education": "Bachelor's",
  "EmploymentType": "Full-time",
  "MaritalStatus": "Divorced",
  "LoanPurpose": "Other",
  "HasMortgage": "Yes",
  "HasDependents": "Yes",
  "HasCoSigner": "Yes"
}
```

### Response

```json
{
  "Default": 1,
  "decision": "will_default",
  "probability": 0.512
}
```

This demonstrates a **borderline risk case**, where the model is uncertain but leans toward default.

---

## 🔧 cURL Example

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "Age": 30,
  "Income": 45000,
  "LoanAmount": 8000,
  "CreditScore": 680,
  "MonthsEmployed": 36,
  "NumCreditLines": 2,
  "InterestRate": 10,
  "LoanTerm": 24,
  "DTIRatio": 0.3,
  "Education": "Master's",
  "EmploymentType": "Full-time",
  "MaritalStatus": "Single",
  "LoanPurpose": "Business",
  "HasMortgage": "No",
  "HasDependents": "No",
  "HasCoSigner": "Yes"
}'
```

---

## 🧩 Tech Stack

* Python
* scikit-learn
* FastAPI
* Pydantic
* Docker
* joblib

---

## 🎯 Project Highlights

* End-to-end ML system
* Strict input validation
* Probability-based predictions
* Dockerized for reproducibility
* Clear API contract
* Production-oriented logging

---

## 📌 Portfolio Note

This project focuses on **ML inference, system design, and deployment**, not just model training.
It demonstrates how machine learning models are **actually used in production systems**.

---

### 👤 Author

**Satadru Halder**

---
