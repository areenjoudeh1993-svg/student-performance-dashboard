from django.shortcuts import render
from .models import Prediction
import joblib
import pandas as pd

model = joblib.load("student_model.pkl")


def home(request):

    df = pd.read_csv(
        "../online_education_dataset.csv"
    )

    total_students = len(df)

    pass_count = len(
        df[df["pass_flag"] == 1]
    )

    fail_count = len(
        df[df["pass_flag"] == 0]
    )

    context = {
        "students": total_students,
        "accuracy": 76.5,
        "pass_count": pass_count,
        "fail_count": fail_count,
    }

    return render(
        request,
        "predictor/home.html",
        context
    )

def prediction(request):

    result = None

    if request.method == "POST":

        studied_credits = float(
            request.POST["studied_credits"]
        )

        total_clicks = float(
            request.POST["total_clicks"]
        )

        avg_score = float(
            request.POST["avg_score"]
        )

        prediction_result = model.predict([
            [
                studied_credits,
                total_clicks,
                avg_score
            ]
        ])

        result = (
            "Pass"
            if prediction_result[0] == 1
            else "Fail"
        )

        Prediction.objects.create(
            studied_credits=studied_credits,
            total_clicks=total_clicks,
            avg_score=avg_score,
            prediction=result
        )

    return render(
        request,
        'predictor/prediction.html',
        {'result': result}
    )