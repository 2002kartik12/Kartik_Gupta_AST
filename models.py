from django.db import models
from db_connection import db


class Job(db.Model):
    job_title = db.CharField(max_length=255)
    company_name = db.CharField(max_length=255)
    location = db.CharField(max_length=255)
    salary = db.CharField(max_length=255)

    def __str__(self):
        return self.job_title
