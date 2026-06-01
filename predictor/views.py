from django.shortcuts import render
from .models import Prediction
import joblib
import pandas as pd

model = joblib.load("student_model.pkl")


def home(request):

    context = {
        "students": 32593,
        "accuracy": 76.5,
        "pass_count": 17000,
        "fail_count": 15593,
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