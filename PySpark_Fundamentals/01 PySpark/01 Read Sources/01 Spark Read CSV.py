# Databricks notebook source
# DBTITLE 1,Reading csv files
#df3 = spark.read.csv("/Volumes/test/test_schema/csv_files/my_files/sales.csv")
#display(df3)

#or
#generic way
df3 = spark.read.format("csv")\
    .option("header","True")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales.csv")
display(df3)

# COMMAND ----------

# DBTITLE 1,applying infer schema
#If we give inferschema, columns will take a particular dataype based on the column values instead of string
df3 = spark.read.format("csv")\
    .option("header","True")\
    .option("inferSchema","True")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales.csv")
display(df3)

# COMMAND ----------

# DBTITLE 1,Method1 of assigning schema before reading the data
#In the above code, price column updated a string, but we want it in double datatype. So, If we know the column names and datatypes in advance, we can create them and then load the data.

schema_str = ("id int, customer_name string, product string, price double, quantity int, remarks string")
df3 = spark.read.format("csv")\
    .schema(schema_str)\
    .option("header","True")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales.csv")
display(df3)
#If we don't know the schema, we can use the above code to infer the schema and then create the dataframe")

"""
#we can also use as below
df3 = spark.read.format("csv")\
    .schema(schema_str)\
    .option("header","False")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales_no_header.csv")
"""

# COMMAND ----------

# DBTITLE 1,Method2 of assigning schema before reading the data
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("remarks", StringType(), True)
])

df3 = spark.read\
    .schema(schema)\
    .option("header","True")\
    .csv("/Volumes/test/test_schema/csv_files/my_files/sales.csv")
display(df3)

#or
#df3 = spark.read.format("csv")\
#    .schema(schema)\
#    .option("header","True")\
#    .csv("/Volumes/test/test_schema/csv_files/my_files/sales.csv")
#display(df3)


# COMMAND ----------

# DBTITLE 1,Working with Delimiter file
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("remarks", StringType(), True)
])

df3 = spark.read\
    .schema(schema)\
    .option("header","True")\
    .option("delimiter","|")\
    .csv("/Volumes/test/test_schema/csv_files/my_files/sales_pipe.csv")
display(df3)

# COMMAND ----------

# DBTITLE 1,working with delimiter file and single quotes
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("remarks", StringType(), True)
])

df3 = spark.read\
    .schema(schema)\
    .option("header","True")\
    .option("delimiter","|")\
    .option("quote","'")\
    .csv("/Volumes/test/test_schema/csv_files/my_files/sales_pipe_single_quote.csv")
display(df3)

# COMMAND ----------

# DBTITLE 1,working with escape character
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("remarks", StringType(), True)
])

df3 = spark.read\
    .schema(schema)\
    .option("header","True")\
    .option("delimiter","|")\
    .option("quote","'")\
    .option("escape","#")\
    .csv("/Volumes/test/test_schema/csv_files/my_files/sales_pipe_single_quote_escape.csv")
display(df3)

# COMMAND ----------

# DBTITLE 1,working with multiline
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("remarks", StringType(), True)
])

df3 = spark.read.format("csv")\
    .schema(schema)\
    .option("header","True")\
    .option("delimiter","|")\
    .option("quote","'")\
    .option("escape","#")\
    .option("multiLine","True")\
    .load("/Volumes/test/test_schema/csv_files/my_files/sales_pipe_single_quote_escape_multiline.csv")
display(df3)