from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("models/rdf.pkl", "rb"))
scaler = pickle.load(open("models/scale1.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/submit", methods=["POST"])
def submit():

    gender = float(request.form["gender"])
    married = float(request.form["married"])
    dependents = float(request.form["dependents"])
    education = float(request.form["education"])
    self_employed = float(request.form["self_employed"])
    applicant_income = float(request.form["applicant_income"])
    coapplicant_income = float(request.form["coapplicant_income"])
    loan_amount = float(request.form["loan_amount"])
    loan_term = float(request.form["loan_term"])
    credit_history = float(request.form["credit_history"])
    property_area = float(request.form["property_area"])

    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    # Scale features
    features = scaler.transform(features)

    # Prediction
    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)