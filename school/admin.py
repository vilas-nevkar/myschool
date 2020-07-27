from django.contrib import admin
from .models import Standard, Student, CastCategory, School, Address, Scheme, Language, Religion


# class Admin()


admin.site.register(Student)
admin.site.register(Standard)
admin.site.register(CastCategory)
admin.site.register(School)
admin.site.register(Address)
admin.site.register(Scheme)
admin.site.register(Language)
admin.site.register(Religion)

