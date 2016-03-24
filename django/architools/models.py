from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

# see spec: https://github.com/gmoulard/OpenStack_Tenant_Doc/blob/master/bd/createtable.sql
# doc https://docs.djangoproject.com/fr/1.9/ref/models/fields/#field-types


# table tenantList(ID, email, ID_T, OS_AUTH_URL, OS_REGION_NAME, OS_TENANT_ID, OS_TENANT_NAME, OS_PROJECT_NAME, OS_USERNAME, OS_PASSWORD, YamlSave, YamlFile)

class TENANTLIST(models.Model):
    EMAIL           = models.CharField(max_length=200)
    OS_AUTH_URL     = models.URLField
    OS_REGION_NAME  = models.CharField(max_length=255)
    OS_TENANT_ID    = models.CharField(max_length=255)
    OS_TENANT_NAME  = models.CharField(max_length=255)
    OS_PROJECT_NAME = models.CharField(max_length=255)
    OS_USERNAME     = models.EmailField
    OS_PASSWORD     = models.CharField(max_length=255)
    YAMLSAVE        = models.TextField
    YAMLFILE        = models.FileField

# table OS_API(ID, API_LIB, API_URL, ORDER)

class OS_API(models.Model):
    API_LIB         = models.CharField(max_length=255)
    API_URL         = models.CharField(max_length=255)
    ORDER           = models.IntegerField

# table APICall(ID, ID_T, DATE_CALL)

class APICALL(models.Model):
    ID_T            = models.ForeignKey(TENANTLIST)
    DATE_CALL       = models.DateTimeField(default=timezone.now)

# table APICall_Memo(ID, ID_CALL, ID_API, VALUE_NAME, VALUE_MEMO)

class APICALL_MEMO(models.Model):
    ID_Call         = models.ForeignKey(APICALL)
    ID_API          = models.ForeignKey(OS_API)
    VALUE_NAME      = models.CharField(max_length=255)
    VALUE_MEMO      = models.CharField(max_length=255)

# table APICallExec(ID, ID_CALL, ID_API,  Json_URLFile, JSON_DATA)

class APICALLEXEC(models.Model):
    ID_Call         = models.ForeignKey(APICALL)
    ID_API          = models.ForeignKey(OS_API)
    JSON_URLFILE    = models.FileField
    JSON_DATA       = models.TextField


# TABLE COMPUTE (ID_CALL, C_ID, C_NAME, ...)

# TABLE SEC_GROUP(ID_CALL, SG_ID, SG_NAME, ...)
# TABLE COMPUTE_SEC_GROUP(ID_CALL, C_ID, SG_ID)
# TABLE SEC_GROUP_RULES(ID_CALL, SG_IG, ...)

# TABLE VOLUMES(ID_CALL, V_ID, V_NAME, C_ID, ...)
# TABLE NETWORK(ID_CALL, ...)
# TABLE SUBNET(ID_CALL, ...)
# TABLE LOADBALANCER (ID_CALL, ...)

