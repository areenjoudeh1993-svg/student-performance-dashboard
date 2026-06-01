from django.db import models

class Prediction(models.Model):

    studied_credits = models.IntegerField()

    total_clicks = models.FloatField()

    avg_score = models.FloatField()

    prediction = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prediction