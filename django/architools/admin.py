from django.contrib import admin

# Register your models here.

from .models import TenantList
admin.site.register(TenantList)

from .models import OS_API
admin.site.register(OS_API)


from .models import APICall
admin.site.register(APICall)


from .models import APICall_Memo
admin.site.register(APICall_Memo)


from .models import APICallExec
admin.site.register(APICallExec)
