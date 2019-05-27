from django.db import models
from inventory.models import Customer, Pop, Core, Device

# Create your models here.
class L2VPN(models.Model):
        channelid = models.CharField(max_length=100)
        channelid.help_text = ''
        channelid.verbose_name = ''
        customer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True)
        coreA = models.ForeignKey(Core, on_delete=models.PROTECT, blank=True, null=True, related_name='l2vpn_coreA')
        coreB = models.ForeignKey(Core, on_delete=models.PROTECT, blank=True, null=True, related_name='l2vpn_coreB')
        pointA = models.ForeignKey(Pop, on_delete=models.PROTECT, blank=True, null=True, related_name='l2vpn_pointA')
        pointB = models.ForeignKey(Pop, on_delete=models.PROTECT, blank=True, null=True,  related_name='l2vpn_pointB')
        deviceA = models.ForeignKey(Device, on_delete=models.PROTECT, blank=True, null=True, related_name='l2vpn_deviceA')
        deviceB = models.ForeignKey(Device, on_delete=models.PROTECT, blank=True, null=True, related_name='l2vpn_deviceB')
        portA = models.CharField(max_length=2, blank=True, null=True)
        portB = models.CharField(max_length=2, blank=True, null=True)
        vlan = models.CharField(max_length=4, blank=True, null=True)
        comments = models.TextField(max_length=1000, blank=True)
        on_date = models.DateField(blank=True, null=True)
        off_date = models.DateField(blank=True, null=True)

        def new_l2vpn(self):
            self.save()

        def __str__(self):
            return self.channelid
