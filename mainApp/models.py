from django.db import models

# Create your models here.
class Problem(models.Model):
    #id_text = models.charField(max_length=200)
    num = models.IntegerField(default=0)
    title = models.CharField(max_length=200)

    def __str__(self):
        return '#%i, title: %s' % (self.num, self.title)

class CompanyTag(models.Model):
    num_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    company_text = models.CharField(max_length=200)

    def __str__(self):
        return 'Company: %s' %(self.company_text)

class CategoryTag(models.Model):
    num_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    category_text = models.CharField(max_length=200)

    def __str__(self):
        return 'Category: %s' % (self.category_text)
