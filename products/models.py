from django.db import models
from django.utils.translation import ugettext_lazy as _

class Catagory(models.Model):
    parent=models.ForeignKey('self',verbose_name=_('parent'),null=True,on_delete=models.CASCADE,blank=True)
    title=models.CharField(verbose_name=_("title"),max_length=50)
    description=models.TextField(verbose_name=_("desctiption"),blank=True)
    avatar=models.ImageField(_("avator"),upload_to="catagories/",blank=True)
    is_enable=models.BooleanField(_("status"),default=True)
    create_date=models.DateTimeField(_("create date"),auto_now_add=True)
    updated_date=models.DateTimeField(_("updated date"),auto_now=True)

    class Meta:
        db_table ="catagories"
        verbose_name=_("Catagory")
        verbose_name_plural=_("Catagories")


class Product(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=50)
    description = models.TextField(verbose_name=_("desctiption"), blank=True)
    avatar = models.ImageField(_("avator"), upload_to="products/", blank=True)
    catagories=models.ManyToManyField('Catagory',verbose_name=_('catagories'),blank=True)
    is_enable = models.BooleanField(_("status"), default=True)
    create_date = models.DateTimeField(_("create date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("updated date"), auto_now=True)

    class Meta:
        db_table ="products"
        verbose_name=_("product")
        verbose_name_plural=_("products")

class File(models.Model):
    product=models.ForeignKey("Product",verbose_name='product',on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("title"), max_length=50)
    file=models.FileField(_('file'),upload_to='file/%y/%m/%d/')
    is_enable = models.BooleanField(_("status"), default=True)
    create_date = models.DateTimeField(_("create date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("updated date"), auto_now=True)

    class Meta:
        db_table ="files"
        verbose_name=_("file")
        verbose_name_plural=_("files")