import os
import sys 
os.environ["SPARK_HOME"]="C:\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder\
    .master("local")\
    .appName("myApp")\
    .config(conf=myConf)\
    .config('spark.sql.warehouse.dir', 'file:///F:\15Mediasoftware\3-1\BigDataProgramming\code\s-201511134\data')\
    .getOrCreate()
    
myspark=spark.sparkContext\
    .textFile(os.path.join("data","ds_spark_spark.txt"))
    
word=myspark\
    .flatMap(lambda x:x.split())\
    .map(lambda x:(x,1))\
    .reduceByKey(lambda x,y:x+y)\
    .map(lambda x:(x[1],x[0]))\
    .sortByKey(False)\
    .take(10)
    
print type(word)
for i in word:
    print i