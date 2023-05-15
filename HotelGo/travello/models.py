from django.db import models

# Create your models here.

class Destination(models.Model):
    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self) -> str:
        return self.name
    def to_dict(self):
        return{
            "name":self.name,
            "img":self.img.url,
            "desc":self.desc,
        }

class Hotel(models.Model):
    name = models.CharField()
    offer = models.BooleanField(default=False)
    rate = models.IntegerField()
    stars=models.IntegerField()
    town = models.CharField()
    dest = models.ForeignKey(Destination,on_delete=models.CASCADE,related_name='Hotel_destination')
    img = models.ImageField(upload_to='pics' ,null=True)

    def to_dict(self):
        return{
            "name" :self.name  ,
            "offer" :self.offer,
            "rate" :self.rate,
            "stars":self.stars,
            "town" :self.town,
            "dest" :self.dest.to_dict(),
            "img" :self.img.url
        }

class Room(models.Model):
     ROOM_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'triple'),
        ('suite', 'Suite'),
    )
     typeOfRoom = models.CharField(max_length=20, choices=ROOM_CHOICES,default=None)
     availability = models.BooleanField()
     hotelRoom = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='Rooms')
     price = models.IntegerField()

     


class FeedBack(models.Model)  : 
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()


