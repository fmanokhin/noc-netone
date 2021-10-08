from django.db import models
from inventory.models import Customer, Pop, Core
from django.core.validators import RegexValidator
ipaddrvalid = RegexValidator(r"^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$")

# Create your models here.
#Модель подсети IPv4
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
    detail = models.TextField(max_length=1000, blank=True)
    tocore = models.ForeignKey(Core, on_delete=models.PROTECT, blank=True, null=True)
    topop = models.ForeignKey(Pop, on_delete=models.PROTECT, blank=True, null=True)
    tocustomer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True)

    def new_network(self):
        self.save()

    def __str__(self):
        return self.network
