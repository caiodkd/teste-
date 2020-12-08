from django.contrib import admin
from .models import Denuncia
from .models import Tipo
from .models import Usuario

admin.site.register(Denuncia)
admin.site.register(Tipo)
admin.site.register(Usuario)


