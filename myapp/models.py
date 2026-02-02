from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToolHistory(models.Model):
    TOOL_CHOICES = [
        ("Grammar Correction", "Grammar Correction"),
        ("Translation", "Translation"),
        ("Tone Changer", "Tone Changer"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.CharField(max_length=50, choices=TOOL_CHOICES)
    input_text = models.TextField()
    output_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tool}"
