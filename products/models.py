from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.CharField(max_length=100)
    rating = models.IntegerField()


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password_id = models.CharField(max_length=16)
    social_login = models.CharField(max_length=2083)
    contact_number = models.CharField(max_length=11)
    house_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=4)
    pin_location = models.CharField(max_length=2083)


class OrderContents(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    order_timestamp = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_name = models.CharField(max_length=255)
    order_total = models.FloatField()


class OrderHistory(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.ForeignKey(OrderContents, on_delete=models.CASCADE)
    order_timestamp = models.CharField(max_length=100)
    discount_type = models.CharField(max_length=50)
    discount_details = models.CharField(max_length=100)
    tax = models.IntegerField()
    order_total = models.FloatField()
    contact_number = models.CharField(max_length=11)
    house_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=4)
    pin_location = models.CharField(max_length=2083)
    shipping_time = models.CharField(max_length=100)
