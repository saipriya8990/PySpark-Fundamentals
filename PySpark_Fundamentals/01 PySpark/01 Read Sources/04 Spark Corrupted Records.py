# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC This video provides a comprehensive guide on identifying and handling corrupted data in *PySpark*, covering common issues in *JSON* and *CSV* formats such as missing quotes, column mismatches, or unexpected characters.
# MAGIC
# MAGIC **Handling Options:**
# MAGIC * **Read Modes:**
# MAGIC     * *Permissive Mode* (Default): Captures malformed records in an `_corrupt_record` column while setting other fields to null.
# MAGIC     * *FailFast Mode*: Immediately stops the process if corruption is detected.
# MAGIC     * *DropMalformed Mode*: Silently skips corrupted records, loading only valid data.
# MAGIC * **Bad Records Path:** An alternative method where corrupt records are stored centrally in a specified external directory as *JSON* files, providing the file path, the corrupted record itself, and the reason for failure.
# MAGIC
# MAGIC **Implementation & Comparison:**
# MAGIC * The video demonstrates these techniques using *Databricks*, showing how to define schemas and use options like `recursiveFileLookup` for centralized error analysis.
# MAGIC * *Option 1* (Read Modes) is best for per-table analysis, while *Option 2* (Bad Records Path) offers a superior central location for debugging issues across multiple datasets.

# COMMAND ----------

# DBTITLE 1,Handle Corrupted data
#default mode is "Permissive Mode". So, a new column was created as "_corrupt_record".
df = spark.read.format("json").load("/Volumes/test/test_schema/json_files/sales_corrupted.json")
display(df)

# COMMAND ----------

# DBTITLE 1,Trying out different modes
"""
df = spark.read.format("json")\
    .option("mode", "PERMISSIVE")\
    .load("/Volumes/test/test_schema/json_files/sales_corrupted.json")
display(df)
"""

df = spark.read.format("json")\
    .option("mode", "FAILFAST")\
    .load("/Volumes/test/test_schema/json_files/sales_corrupted.json")
display(df)

# COMMAND ----------

# DBTITLE 1,Trying out different modes in json format
#dropped corrupted records
df = spark.read.format("json")\
    .option("mode", "DROPMALFORMED")\
    .load("/Volumes/test/test_schema/json_files/sales_corrupted.json")
display(df)

# COMMAND ----------

# DBTITLE 1,reading csv file without any mode

#by default, no corrupted column names or values are displayed
df = spark.read.format("csv")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales_corrupted.csv")
display(df)

# COMMAND ----------

# DBTITLE 1,Reading csv file in permissive mode

#In csv, only the corrupted value in a column will update as NULL, but in JSON, whole row will be null
#In "DROPMALFORMED", no need to use "_corrupt_record" column as corrupted records will be dropped.
schema_str = ("id int, customer_name string, product string, price double, quantity int, remarks string, _corrupt_record string ")

df = spark.read.format("csv")\
    .schema(schema_str)\
    .option("mode", "PERMISSIVE")\
    .option("header", "true")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales_corrupted.csv")
display(df)

# COMMAND ----------

# DBTITLE 1,Reading csv file and sending bad records to a file
schema_str = ("id int, customer_name string, product string, price double, quantity int, remarks string")

df = spark.read.format("csv")\
    .schema(schema_str)\
    .option("header", "true")\
    .option("badRecordsPath", "/Volumes/test/test_schema/csv_files/my_files/bad_records")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales_corrupted.csv")
display(df)

# COMMAND ----------

# DBTITLE 1,Reading the bad record file created from above step
df = spark.read.format("json")\
    .option("recursiveFileLookup", "true")\
    .load("/Volumes/test/test_schema/csv_files/my_files/bad_records")
display(df)