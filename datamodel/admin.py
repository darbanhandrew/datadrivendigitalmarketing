from django.contrib import admin

# Register your models here.
from .models import Channel

admin.site.register(Channel)

from .models import Content

admin.site.register(Content)

from .models import Step

admin.site.register(Step)

from .models import IdealCube

admin.site.register(IdealCube)

from .models import RealCube

admin.site.register(RealCube)
