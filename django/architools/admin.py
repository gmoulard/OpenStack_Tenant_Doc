from django.contrib import admin

# Register your models here.

from .models import TENANTLIST
admin.site.register(TENANTLIST)

from .models import OS_API
admin.site.register(OS_API)


from .models import APICALL
admin.site.register(APICALL)


from .models import APICALL_MEMO
admin.site.register(APICALL_MEMO)


from .models import APICALLEXEC
admin.site.register(APICALLEXEC)
