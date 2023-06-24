from django.db import models

class Users(models.Model):
    name = models.CharField(("Display Name"), max_length=50)
    email = models.EmailField(max_length=254)
    urllist = models.URLField(("URL"), max_length=200)
    interval = models.CharField(max_length=10, choices = [('Daily', 'daily'), ('Weekly', 'weekly'), ('Monthly', 'monthly')])
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string that confirms the form was submitted successfully"""
        return f"Successfully subscribed to recieve job postings from {self.urllist} {self.interval}"


