from django.db import models

class Stock(models.Model):
    STOCK_UPDATER = [('IBO', 'IDAN'), ('SEF', 'Sefi')]
    ticker = models.CharField(max_length=6)
    company = models.CharField(max_length=100, blank=True)
    updater = models.CharField(choices=STOCK_UPDATER, max_length=3)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    notes = models.ManyToManyField('Note', blank=True)
    exchange = models.ForeignKey('Exchange', on_delete=models.CASCADE, blank=True)

class Exchange(models.Model):
    ticker = models.CharField(max_length=6)
    name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
      return self.ticker
    
    

class Note(models.Model):
    title = models.CharField(max_length=100)
    note_text = models.TextField(blank=True)
    submition_date = models.DateTimeField(blank=True)

    def __str__(self):
      return self.title