from django.db import models

# Create your models here.


Cars_Models = (
        ("1" , "فيات") ,
        ("2","مرسيدس") ,
        ("3" ,"بي ام دابليو" ) ,
        ("4","دايو") ,
        ("5","متسوبيشي") ,
        ("6","كيا") ,
        ("7","تيوتا") ,
        ("8","بيجو") ,
        ("9","أخري")
    )


TRIPKIND= (
        ("1","المنيا"),
        ("2","القاهرة")
        )


UserMode =(
("1","شير بنزين"),
("2","شركة سفريات")
)

class Profile(models.Model):
    user_name    = models.CharField(max_length =150)
    phone_number = models.CharField(max_length = 20)
    cars_model =   models.CharField(max_length = 20 , choices=Cars_Models ,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)



class Journey(models.Model):
    user_name    = models.CharField(max_length =150)
    phone_number = models.CharField(max_length = 20)
    cars_model =   models.CharField(max_length = 20 , choices=Cars_Models ,null=True,blank=True)
    go_from  = models.CharField(max_length = 20 , choices=TRIPKIND )
    journey_kind  = models.CharField(max_length = 20 , choices=UserMode )
    date = models.DateField()
    start_range = models.TimeField()
    end_range = models.TimeField()
    available_places = models.IntegerField()
    share_price = models.IntegerField()
    travieler = models.ManyToManyField(Profile , null=True,blank=True)
