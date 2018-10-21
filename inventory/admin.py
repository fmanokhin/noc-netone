from django.contrib import admin
from .models import Pop, Core, Customer, Device, Network, Host
# Register your models here.
admin.site.register(Pop)
admin.site.register(Core)
admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(Network)
admin.site.register(Host)
