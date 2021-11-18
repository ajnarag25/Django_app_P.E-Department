from django.contrib import admin

from .models import Registration, Buy, Reserve, Borrow

# Register your models here.
admin.site.register(Registration)
admin.site.register(Buy)
admin.site.register(Reserve)
admin.site.register(Borrow)
