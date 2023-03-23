from io import BytesIO
from PIL import Image

from django.db import models
from urllib import request
from django.core.files import File


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField()
    thumbnail = models.URLField()
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.TextField(max_length=180)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #print f'/{self.category.slug}/{self.slug}/'
        return f'/{self.category}/{self.slug}/'
        
       #return '/%s/%s/' % (self.category.slug, self.slug)

    def get_image(self):
       # print ( )
        print ( self.image)
        print ('Current URL is '+ self.image)
        if self.image:
            #return  self.image.url
        
           #return 'http://127.0.0.1:8000' + self.image.url
            #result = request.urlretrieve(self.image)
            #print ('Result1 is -'+result)
            return  self.image
           
        else:
          return ''



    def get_thumbnail(self):
        if self.thumbnail:
            #return  'http://127.0.0.1:8000' +self.thumbnail.url
            print ('Thumbnail url- '+(self.thumbnail))
            return (self.thumbnail) #self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                #return  'http://127.0.0.1:8000' + self.thumbnail.url
                return   self.thumbnail
               
            else:
                return ''

    def make_thumbnail(self, image):
        img = Image.open(image)
        img.convert('RGB')
        width, height = img.size
        square_size = min(img.size)

        left = (width - square_size) // 2
        top = (height - square_size) // 2
        right = (width + square_size) // 2
        bottom = (height + square_size) // 2

        img = img.crop((left, top, right, bottom))

        img.thumbnail((480, 480))

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=180)
    slug = models.CharField(max_length=50)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
