from django.db import models
from django.core.validators import RegexValidator
ipaddrvalid = RegexValidator(r"^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$")
# Create your models here.
# Модель узла
class Core(models.Model):
    title = models.CharField(max_length=100, blank=True)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    devices = models.ManyToManyField('Device', blank=True)
    devices.help_text = ''
    devices.verbose_name = ''
    downstream = models.ManyToManyField('Pop', blank=True)
    downstream.help_text = ''
    downstream.verbose_name = ''

    def new_core(self):
        self.save()

    def __str__(self):
        return self.title

# Модель точки присутствия
class Pop(models.Model):
    title = models.CharField(max_length=100, blank=True)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100, blank=True)
    manager = models.CharField(max_length=100)
    bandwidth = models.CharField(max_length=100, blank=True)
    vlans = models.CharField(max_length=100)
    comments = models.CharField(max_length=100, blank=True)
    devices = models.ManyToManyField('Device', blank=True)
    devices.help_text = ''
    devices.verbose_name = ''
    upstream = models.ManyToManyField(Core, blank=True)
    upstream.help_text = ''
    upstream.verbose_name = ''
    downstream = models.ManyToManyField('Customer', blank=True)
    downstream.help_text = ''
    downstream.verbose_name = ''

    def new_pop(self):
        self.save()

    def __str__(self):
        return self.title

#Модель Клиента
class Customer(models.Model):
    title = models.CharField(max_length=100, blank=True)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    comments = models.CharField(max_length=100, blank=True)
    upstream = models.ManyToManyField(Pop, blank=True)
    upstream.help_text = ''
    upstream.verbose_name = ''
    #поле "подключение" на странице клиента
    switch = models.CharField(max_length=100)
    vlans = models.CharField(max_length=100)
    bandwidth = models.CharField(max_length=100)

    def new_customer(self):
        self.save()

    def __str__(self):
        return self.title

class Device(models.Model):
    vendor = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dnsname = models.CharField(max_length=100, blank=True)
    dnsname.help_text = ''
    dnsname.verbose_name = ''
    ipaddress = models.CharField(max_length=100)
    geoaddress = models.CharField(max_length=100)
    coreaddress = models.ManyToManyField(Core, blank='True')
    coreaddress.help_text = ''
    coreaddress.verbose_name = ''
    address = models.ManyToManyField(Pop, blank='True')
    address.help_text = ''
    address.verbose_name = ''

    def new_device(self):
        self.save()

    def __str__(self):
        return self.dnsname

class Network(models.Model):
    network = models.CharField(max_length=18, validators=[ipaddrvalid])
    comment = models.CharField(max_length=100, blank=True)

    def new_network(self):
        self.save()

    def __str__(self):
        return self.network
