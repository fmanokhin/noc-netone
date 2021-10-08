from django.db import models

#Create your models here.
#Модель узла
class Core(models.Model):
    title = models.CharField(max_length=100)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.TextField(max_length=1000, blank=True)
    manager = models.CharField(max_length=100, blank=True)
    bandwidth = models.CharField(max_length=100, blank=True)
    vlans = models.CharField(max_length=100, blank=True)
    comments = models.TextField(max_length=1000, blank=True)
    downstream = models.ManyToManyField('Pop', blank=True)
    downstream.help_text = ''
    downstream.verbose_name = ''

    def new_core(self):
        self.save()

    def __str__(self):
        return self.title

#Модель точки присутствия
class Pop(models.Model):
    title = models.CharField(max_length=100)
    title.help_text = ''
    title.verbose_name = ''
    address = models.CharField(max_length=100)
    contacts = models.TextField(max_length=1000, blank=True)
    manager = models.CharField(max_length=100, blank=True)
    bandwidth = models.CharField(max_length=100, blank=True)
    vlans = models.CharField(max_length=100, blank=True)
    comments = models.TextField(max_length=1000, blank=True)
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
    contacts = models.TextField(max_length=1000, blank=True)
    manager = models.CharField(max_length=100, blank=True)
    comments = models.TextField(max_length=1000, blank=True)
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
    FREE = 'FREE'
    BUSY = 'BUSY'
    STATUS_CHOISES = (
        (FREE, 'Свободно'),
        (BUSY, 'Установлено'),
    )
    status = models.CharField(max_length=4, choices=STATUS_CHOISES, default=FREE)
    vendor = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dnsname = models.CharField(max_length=100, blank=True)
    dnsname.help_text = ''
    dnsname.verbose_name = ''
    ipaddress = models.CharField(max_length=100)
    comments = models.CharField(max_length=100, blank=True)
    serialnum = models.CharField(max_length=100, blank=True)
    tocore = models.ForeignKey(Core, on_delete=models.PROTECT, blank=True, null=True)
    topop = models.ForeignKey(Pop, on_delete=models.PROTECT, blank=True, null=True)

    def new_device(self):
        self.save()

    def __str__(self):
        return self.dnsname
