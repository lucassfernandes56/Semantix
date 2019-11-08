from pyspark import SparkConf, SparkContext
from operator import add

spark_conf = (SparkConf()
         .setMaster("local[4]")
         .setAppName("Semantix challenge"))
sc = SparkContext(conf = spark_conf)

july = sc.textFile('data/NASA_access_log_Jul95')
july = july.cache()

august = sc.textFile('data/NASA_access_log_Aug95')
august = august.cache()

# number of distinct hosts
july_count = july.flatMap(lambda line: line.split(' ')[0]).distinct().count()
august_count = august.flatMap(lambda line: line.split(' ')[0]).distinct().count()
print('Distinct hosts on July: %s' % july_count)
print('Distinct hosts on August %s' % august_count)

sc.stop()