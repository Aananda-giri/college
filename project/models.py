from django.db import models

# Create your models here.

class Queries(models.Model):
    query = models.CharField(max_length=100)
    def print_queries():
        results = Queries.objects.raw('SELECT * FROM project_queries')
        print(f'\n ---{results}--- \n')
        return results
        pass

