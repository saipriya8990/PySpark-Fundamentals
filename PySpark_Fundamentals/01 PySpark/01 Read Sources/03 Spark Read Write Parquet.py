# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC **Parquet file format**
# MAGIC A highly efficient columnar data storage solution for modern data engineering. Parquet is designed for fast data retrieval and significant storage savings compared to row-oriented formats like *CSV* or *JSON*.
# MAGIC
# MAGIC **Key Advantages of Parquet:**
# MAGIC * **Storage Efficiency:** Converting data from *CSV* to *Parquet* can save up to 87% of storage space.
# MAGIC * **Faster Performance:** Queries run significantly faster, with the video noting up to 34 times faster performance than *CSV* for specific analytical tasks.
# MAGIC * **Data Skipping:** Thanks to *footers* containing metadata and statistics (min/max values, null counts), *Parquet* can skip files that do not contain the required data, leading to massive reductions in data read.
# MAGIC
# MAGIC **Structural Details:**
# MAGIC * **Columnar vs. Row Storage:** While *CSV* stores data row-by-row, *Parquet* organizes data by column. This allows systems to read only the specific columns needed for a query, rather than scanning the entire file.
# MAGIC * **Row Groups & Footers:** Data is organized into *row groups*, and each file includes a *footer* acting as an index that provides essential metadata about the column types, encoding, and statistical profiling.
# MAGIC
# MAGIC **Hands-on with PySpark:**
# MAGIC * **Writing Data:** The video demonstrates how to convert a *JSON* file to *Parquet* using `df.write.format('parquet').save()` in *Databricks*.
# MAGIC * **Reading Data:** You can load *Parquet* files back into a *Spark DataFrame* using `spark.read.format('parquet').load()`, including the ability to read entire folders at once.

# COMMAND ----------

# DBTITLE 1,Converting Json file to parquet format
df = spark.read.format("json").load("/Volumes/test/test_schema/json_files/sales_single_line.json")
#display(df)

df.write.format("parquet").save("/Volumes/test/test_schema/json_files/parquet_output")

# COMMAND ----------

# DBTITLE 1,Reading parquet file
df=spark.read.format("parquet").load("/Volumes/test/test_schema/json_files/parquet_output")
display(df)