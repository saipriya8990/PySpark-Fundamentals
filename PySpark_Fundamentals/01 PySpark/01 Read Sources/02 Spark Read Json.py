# Databricks notebook source
# DBTITLE 1,Reading single line JSON file

#df= spark.read.json("/Volumes/test/test_schema/json_files/sales_single_line.json")

df = spark.read.format("json")\
    .load("/Volumes/test/test_schema/json_files/sales_single_line.json")
display(df)

# COMMAND ----------

# DBTITLE 1,Reading a multiline json file
df = spark.read.format("json")\
    .option("multiLine","True")\
    .load("/Volumes/test/test_schema/json_files/sales_multi_line.json")
#display(df)

df.write.format("json")\
    .save("/Volumes/test/test_schema/json_files/json_output")

# COMMAND ----------

# DBTITLE 1,Can also write as csv file from JSON file
df.write.format("csv")\
    .save("/Volumes/test/test_schema/json_files/csv_output")