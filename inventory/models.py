from django.db import models
from django.core.validators import RegexValidator
ipaddrvalid = RegexValidator(r"^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$")
#Create your models here.
# Модель узла
class Core(models.Model):
    title = models.CharField(max_length=100)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100, blank=True)
    manager = models.CharField(max_length=100, blank=True)
    bandwidth = models.CharField(max_length=100, blank=True)
    vlans = models.CharField(max_length=100, blank=True)
    comments = models.TextField(max_length=100, blank=True)
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
    title = models.CharField(max_length=100)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100, blank=True)
    manager = models.CharField(max_length=100, blank=True)
    bandwidth = models.CharField(max_length=100, blank=True)
    vlans = models.CharField(max_length=100, blank=True)
    comments = models.TextField(max_length=100, blank=True)
    devices = models.ManyToManyField('Device', blank=True)
    devices.help_text = ''
    devices.verbose_name = ''
    upstream = models.ManyToManyField(Core, blank=True)
    upstream.help_text = ''
    upstream.verbose_name = ''
    otherpopsupstream = models.ManyToManyField('Pop', related_name='otherpops_upstream')
    otherpopsupstream.help_text = ''
    otherpopsupstream.verbose_name = ''
    otherpopsdownstream = models.ManyToManyField('Pop', related_name="otherpops_downstream")
    otherpopsdownstream.help_text = ''
    otherpopsdownstream.verbose_name = ''
    downstream = models.ManyToManyField('Customer', blank=True)
    downstream.help_text = ''
    downstream.verbose_name = ''

    def new_pop(self):
        self.save()

    def __str__(self):
        return self.title

#Модель Клиента
class Customer(models.Model):
    title = models.CharField(max_length=100)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100, blank=True)
    manager = models.CharField(max_length=100, blank=True)
    comments = models.TextField(max_length=100, blank=True)
    upstream = models.ManyToManyField(Pop, blank=True)
    upstream.help_text = ''
    upstream.verbose_name = ''
    #поле "подключение" на странице клиента
    switch = models.CharField(max_length=100, blank=True)
    vlans = models.CharField(max_length=100, blank=True)
    bandwidth = models.CharField(max_length=100, blank=True)

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
    coreaddress = models.ManyToManyField(Core, blank=True)
    coreaddress.help_text = ''
    coreaddress.verbose_name = ''
    address = models.ManyToManyField(Pop, blank=True)
    address.help_text = ''
    address.verbose_name = ''

    def new_device(self):
        self.save()

    def __str__(self):
        return self.dnsname


class Network(models.Model):
    FREE = 'FREE'
    BUSY = 'BUSY'
    STATUS_CHOISES = (
        (FREE, 'Свободно'),
        (BUSY, 'Занято'),
    )
    MPLS = 'MPLS'
    TECH = 'TECH'
    CORE = 'CORE'
    CUSTOMER = 'Customers'
    SEGMENT_CHOISES = (
        (TECH, 'TECH'),
        (MPLS, 'MPLS'),
        (CORE, 'CORE'),
        (CUSTOMER, 'CUSTOMERS'),
    )
    network = models.CharField(max_length=18, validators=[ipaddrvalid])
    status = models.CharField(max_length=4, choices=STATUS_CHOISES, default=FREE)
    segment = models.CharField(max_length=9, choices=SEGMENT_CHOISES)
    comment = models.CharField(max_length=100, blank=True)
    tocore = models.ForeignKey(Core, on_delete=models.PROTECT, blank=True, null=True)
    topop = models.ForeignKey(Pop, on_delete=models.PROTECT, blank=True, null=True)
    tocustomer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True)

    def new_network(self):
        self.save()

    def __str__(self):
        return self.network
