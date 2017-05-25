
import os
lines=spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki.txt"))
wc=lines\
    .flatMap(lambda x: x.split(' '))
print type(wc)

from operator import add
wc = spark.sparkContext.textFile("data/ds_spark_wiki.txt")\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])

for e in wc.collect():
    print e
    
documents = spark.sparkContext.textFile("data/ds_spark_wiki.txt")\
    .map(lambda line: line.split(" "))
    
from pyspark.mllib.feature import HashingTF

hashingTF = HashingTF()
tf = hashingTF.transform(documents)
tf.collect()