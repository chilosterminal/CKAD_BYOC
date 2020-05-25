from django.db import models

class Questions(models.Model):
    categories = [('1', 'Core Concepts'), ('2', 'Configuration'), ('3', "Multi-Container Pods"), ('4', 'Observability'), ('5', 'Pod Design'), ('6', 'Services and Networking'), ('7', 'State Persistence')]
    name_short = models.CharField(max_length=60)
    question = models.CharField(max_length=450)
    category = models.CharField(choices=categories, max_length=30)
    submission_date = models.DateTimeField()
    nscontext = models.CharField(max_length=20)
    context = models.CharField(max_length=20)
    workdir = models.CharField(max_length=20)

