from django.db import models

class Drama(models.Model):
    drama_code = models.CharField(max_length=30)
    story = models.TextField()

    def __unicode__(self):
        return self.drama_code

class PPL(models.Model):
    drama_code = models.CharField(max_length=30)
    product_code = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.drama_code, self.product_code)

class Product(models.Model):
    drama_code = models.CharField(max_length=30)
    product_code = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=60)
    product_image = models.URLField()
    brand_name = models.CharField(max_length=40)
    store_link = models.URLField()
    price = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.drama_code, self.product_code)
