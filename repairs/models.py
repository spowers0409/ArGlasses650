from django.db import models

class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.trim}"

class RepairType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Repair(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    repair_type = models.ForeignKey(RepairType, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.vehicle} - {self.repair_type} - {self.description}"
