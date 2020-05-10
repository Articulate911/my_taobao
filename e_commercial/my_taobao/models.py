from django.db import models
from django.contrib.auth.models import User

class Commodity(models.Model):
    commodity_id = models.PositiveIntegerField(db_column='commodity_ID', primary_key=True)  # Field name made lowercase.
    commodity_catalog_code = models.ForeignKey('CommodityCatalog', models.DO_NOTHING, db_column='commodity_catalog_code')
    commodity_name = models.CharField(max_length=45)
    price = models.FloatField()
    place_of_delivery = models.CharField(max_length=45, blank=True, null=True)
    commodity_specification = models.CharField(max_length=45, blank=True, null=True)
    commodity_introduction = models.CharField(max_length=2048, blank=True, null=True)
    shop_id = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_id')
    class Meta:
        managed = False
        db_table = 'commodity'


class CommodityCatalog(models.Model):
    commodity_catalog_code = models.PositiveIntegerField(primary_key=True)
    commodity_catalog_name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'commodity_catalog'


class Follow(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_ID')  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'follow'


class OrderForm(models.Model):
    order_form_id = models.PositiveIntegerField(db_column='order_form_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    order_form_catalog_code = models.ForeignKey('OrderFormCatalog', models.DO_NOTHING, db_column='order_form_catalog_code')
    freight = models.FloatField()
    create_time = models.DateTimeField()
    pay_time = models.DateTimeField(blank=True, null=True)
    deliver_time = models.DateTimeField(blank=True, null=True)
    deal_time = models.DateTimeField(blank=True, null=True)
    receive_address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order_form'


class OrderFormCatalog(models.Model):
    order_form_catalog_code = models.CharField(primary_key=True, max_length=1)
    order_form_catalog_name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'order_form_catalog'


class OrderFormCommodity(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    order_form = models.ForeignKey(OrderForm, models.DO_NOTHING, db_column='order_form_ID')  # Field name made lowercase.
    commodity = models.ForeignKey(Commodity, models.DO_NOTHING, db_column='commodity_ID')  # Field name made lowercase.
    commodity_pc = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'order_form_commodity'


class Refund(models.Model):
    refund_id = models.PositiveIntegerField(db_column='refund_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    commodity = models.ForeignKey(Commodity, models.DO_NOTHING, db_column='commodity_ID')  # Field name made lowercase.
    refund_reason = models.CharField(max_length=50)
    refund_quantity = models.PositiveIntegerField()
    apply_time = models.DateTimeField()
    refund_time = models.DateTimeField(blank=True, null=True)
    refund_catalog = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'refund'


class Sells(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    commodity = models.ForeignKey(Commodity, models.DO_NOTHING, db_column='commodity_ID')  # Field name made lowercase.
    shop = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_ID')  # Field name made lowercase.
    inventory = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'sells'


class Shop(models.Model):
    shop_id = models.PositiveIntegerField(db_column='shop_ID', primary_key=True)  # Field name made lowercase.
    shop_name = models.CharField(max_length=45)
    shop_reg_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'shop'


class ShoppingCart(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    commodity = models.ForeignKey(Commodity, models.DO_NOTHING, db_column='commodity_ID')  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shopping_cart'