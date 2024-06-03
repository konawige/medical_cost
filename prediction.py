import joblib
def predict(data):
    clf = joblib.load("my_insurance_ml.pkl")
    return clf.predict(data)