from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

# see spec: https://github.com/gmoulard/OpenStack_Tenant_Doc/blob/master/bd/createtable.sql
# doc https://docs.djangoproject.com/fr/1.9/ref/models/fields/#field-types


# table tenantList(ID, email, ID_T, OS_AUTH_URL, OS_REGION_NAME, OS_TENANT_ID, OS_TENANT_NAME, OS_PROJECT_NAME, OS_USERNAME, OS_PASSWORD, YamlSave, YamlFile)

class TenantList(models.Model):
    email           = models.CharField(max_length=200)
    OS_AUTH_URL     = models.URLField
    OS_REGION_NAME  = models.CharField(max_length=255)
    OS_TENANT_ID    = models.CharField(max_length=255)
    OS_TENANT_NAME  = models.CharField(max_length=255)
    OS_PROJECT_NAME = models.CharField(max_length=255)
    OS_USERNAME     = models.EmailField
    OS_PASSWORD     = models.CharField(max_length=255)
    YamlSave        = models.TextField
    YamlFile        = models.FileField


# table OS_API(ID, API_LIB, API_URL, ORDER)

class OS_API(models.Model):
    API_LIB         = models.CharField(max_length=255)
    API_URL         = models.CharField(max_length=255)
    ORDER           = models.IntegerField

# table APICall(ID, ID_T, DATE_CALL)

class APICall(models.Model):
    ID_T            = models.ForeignKey(TenantList)
    DATE_CALL       = models.DateTimeField(default=timezone.now)


# table APICall_Memo(ID, ID_CALL, ID_API, VALUE_NAME, VALUE_MEMO)

class APICall_Memo(models.Model):
    ID_Call         = models.ForeignKey(APICall)
    ID_API          = models.ForeignKey(OS_API)
    VALUE_NAME      = models.CharField(max_length=255)
    VALUE_MEMO      = models.CharField(max_length=255)

# table APICallExec(ID, ID_CALL, ID_API,  Json_URLFile, JSON_DATA)
class APICallExec(models.Model):
    ID_Call         = models.ForeignKey(APICall)
    ID_API          = models.ForeignKey(OS_API)
    Json_URLFile    = models.FileField
    Json_Data       = models.TextField

# table compute (ID_CALL, C_ID, C_NAME, ...)

# table sec_group(ID_CALL, SG_ID, SG_NAME, ...)
# table compute_sec_group(ID_CALL, C_ID, SG_ID)
# table sec_group_rules(ID_CALL, SG_IG, ...)

# table volumes(ID_CALL, V_ID, V_NAME, C_ID, ...)
# table network(ID_CALL, ...)
# table subnet(ID_CALL, ...)
# table loadBalancer (ID_CALL, ...)

