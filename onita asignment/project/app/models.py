from django.db import models

class movies(models.Model):
    tconts = models.CharField(max_length=500,null=True,blank= True)
    titleType = models.CharField(max_length=500,null=True,blank= True)
    primaryTitle = models.CharField(max_length=50,null=True,blank= True)
    runtimeMinutes = models.IntegerField()
    genres = models.CharField(max_length=100 ,null =True,blank=True)


    def __str__(self):
        return str(self.primaryTitle)
    

class ratings(models.Model):
    tconst = models.CharField(max_length=100,null=True,blank=True)
    averageRating = models.FloatField(null=True,blank=True)
    numVotes = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.averageRating)
     

   


    