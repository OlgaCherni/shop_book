from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name                     # визуал в админке


class Author(models.Model):                             
    name = models.CharField(max_length=60, verbose_name= "Имя")
    second_name = models.CharField(max_length=60, verbose_name= "Отчество", null=True, blank=True)
    surname = models.CharField(max_length=60, verbose_name= "Фамилия")
    
    def __str__(self):
        return f"{self.surname} {self.name[0]}.{self.second_name[0]}."                


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)          
    name = models.CharField(max_length=60)
    date_of_birth = models.IntegerField()
    image = models.ImageField(upload_to="media", null=True, blank=True )
    info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.author}"
    



















    # image = models.ImageField(null=True, blank=True)
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url
