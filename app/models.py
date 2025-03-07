from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)  
    age = models.IntegerField() 
    gender = models.CharField(max_length=20)  
    weight = models.DecimalField(max_digits=5, decimal_places=2)  
    heart_rate = models.IntegerField(null=True, blank=True)
    blood_pressure = models.IntegerField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True) 
    chief_complaint_chest_pain = models.BooleanField(default=False)
    chief_complaint_fever = models.BooleanField(default=False)
    chief_complaint_headache = models.BooleanField(default=False)
    chief_complaint_difficulty_breathing = models.BooleanField(default=False)
    chief_complaint_abdominal_pain = models.BooleanField(default=False)
    severity = models.CharField(max_length=50, default="Unknown")

    def __str__(self):
        return f"Patient {self.id}: \n Name: {self.name} - Severity: {self.severity}"
    
    class Meta:
        db_table = "patients"  # Optional: Explicitly setting table name (not required)
        managed=True
