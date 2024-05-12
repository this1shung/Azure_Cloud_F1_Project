# Databricks notebook source
client_id = dbutils.secrets.get(scope = 'formular1-scope', key = 'formula1-app-client-id')
tenant_id = dbutils.secrets.get(scope = 'formular1-scope', key = 'formula1-app-tenant-id')
client_secret = dbutils.secrets.get(scope = 'formular1-scope', key = 'formula1-app-client-secret')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.hungdatalakegen2.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.hungdatalakegen2.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.hungdatalakegen2.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.hungdatalakegen2.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.hungdatalakegen2.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://presentation@hungdatalakegen2.dfs.core.windows.net")

# COMMAND ----------

