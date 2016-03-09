# gmoulard - je ne me rappel plus trop comment ont fait les create table alors, je ne fait que des commentaires :)

# table applicationUser(email, shaPassword, nom, pnom, tokenValidated)
# mettre validated dans tokenValidated aprés validation du token ou une clef ramdom pour le token de validation

# table tenantList(email, ID_T, OS_AUTH_URL, OS_REGION_NAME, OS_TENANT_ID, OS_TENANT_NAME, OS_PROJECT_NAME, OS_USERNAME, OS_PASSWORD, YamlSave)
# table API(ID_API, API_LIB, API_URL, ORDER)

# table APICall(ID_CALL, ID_T, DATE_CALL)

# table APICall_Memo(ID_CALL, ID_API, VALUE_NAME, VALUE_MEMO)
# table APICallExec(ID_CALL, ID_API,  JSON_URL_STORAGE_NAME, JSON_DATA)

# table compute (ID_CALL, C_ID, C_NAME, ...)

# table sec_group(ID_CALL, SG_ID, SG_NAME, ...)
# table compute_sec_group(ID_CALL, C_ID, SG_ID)
# table sec_group_rules(ID_CALL, SG_IG, ...)

# table volumes(ID_CALL, V_ID, V_NAME, C_ID, ...)
# table network(ID_CALL, ...)
# table subnet(ID_CALL, ...)
# table loadBalancer (ID_CALL, ...)

#
