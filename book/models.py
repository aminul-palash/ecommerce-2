from django.db import models

# Create your models here.
LANGUAGE_CHOICES = (
("BANGLA", "Bangla"),
("ENGLISH", "English"),
("ARABIC","Arabic"),
("URDU", "Urdu"),
)
CATEGORY_CHOICES = (
("Spirituality", "Spirituality"),
("Tafseer", "Tafseer"),
("Hadith","Hadith"),
("Aqeedah", "Aqeedah"),
)
PUBLICATION_CHOICES = (
  ("None","None"),
   ("A","A"),
   ("B","B"),
   ("C","C"),
)

class Book(models.Model):
    title            = models.CharField(max_length=32)
    language         = models.CharField(max_length=32,choices=LANGUAGE_CHOICES,default="BANGLA")
    category         = models.CharField(max_length=32,choices=CATEGORY_CHOICES,default="Spirituality")
    publication      = models.CharField(max_length=32,choices = PUBLICATION_CHOICES,default="None")
    details          = models.TextField()
    Author           = models.CharField(max_length=32)
    image            = models.ImageField(upload_to='%Y/%m/%d')
    
    def __str__(self):
        return str(self.title)