from django.db import models
from helpers.models import BaseModel
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import User
from django.utils.translation import gettext as _



class Category(BaseModel):
    title = models.CharField(help_text=_('This is the help text'),max_length=256)
    slug = models.CharField(max_length=256)
    icon = models.FileField(upload_to="category/", null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True,on_delete=models.CASCADE,)


class Product(BaseModel):
    title = models.CharField(help_text=_('This is the help text'),max_length=256)
    slug = models.CharField(max_length=256)
    content = RichTextUploadingField()
    image = models.ImageField(
        upload_to="product_image", editable=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    in_stock = models.IntegerField(default=0)

    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Sotilish narxi")
    price_discount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True, blank=True, verbose_name="Chegirmadagi narxi(ustiga chizilgan)")

    rate = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    saveds = models.ManyToManyField(User, related_name="saved_products")

    def set_image(self):
        main_image = ProductImage.objects.filter(
            product=self, is_main=True).first()
        self.image = main_image
        self.save()

class Option(BaseModel):
    title = models.CharField(max_length=200)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)

class OptionValue(BaseModel):
    title = models.CharField(max_length=200)
    option = models.ForeignKey(Option,on_delete=models.CASCADE)
    
class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_image/")
    is_main = models.BooleanField(default=False)
    
    options = models.ManyToManyField(OptionValue)


class Comment(BaseModel):
    product = models.ForeignKey(Product,related_name="comments",on_delete=models.CASCADE )
    user = models.ForeignKey(
        User, related_name="comments",on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    content = models.TextField()





# SIGNAL
# comment count, rate.
