from django.db import models

class Projeto(models.Model):

    risk_choice = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2")
    )

    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=100, null=False)
    ProjectBeginning = models.DateField(null=False)
    ProjectEnd = models.DateField(null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Value = models.DecimalField(max_digits=12, decimal_places=3, null=False)
    Risk = models.IntegerField(max_length=1, choices=risk_choice, null=False)
    Participants = models.TextField(null=False)