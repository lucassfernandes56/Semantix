# Datasets:
# 	July -> ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz
# 	August -> ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz

from pyspark import SparkConf, SparkContext
from operator import add

spark_conf = (SparkConf()
         .setMaster("local[4]")
         .setAppName("Semantix challenge"))
sc = SparkContext(conf = spark_conf)

dataset_july = sc.textFile('data/NASA_access_log_Jul95')
dataset_july.cache()
dataset_august = sc.textFile('data/NASA_access_log_Aug95')
dataset_august.cache()

# combine both datasets
dataset = dataset_july.union(dataset_august)
dataset = dataset.cache()

# number of distinct hosts
hosts_count = dataset.flatMap(lambda line: line.split(' ')[0]).distinct().count()
print('Distinct hosts: %s' % hosts_count)

# number of 404 errors
def response_code_404(line):
    try:
        code = line.split(' ')[-2]
        if code == '404':
            return True
    except:
        pass
    return False

total_errors_404 = dataset.filter(response_code_404).cache()
print('total 404 errors %s' % total_errors_404.count())

# 5 most frequent endpoints causing 404 errors
def top_five_endpoints(rdd):
    endpoints = rdd.map(lambda line: line.split('"')[1].split(' ')[1])
    counts = endpoints.map(lambda endpoint: (endpoint, 1)).reduceByKey(add)
    top_five = counts.sortBy(lambda pair: -pair[1]).take(5)
    return top_five

top_five = top_five_endpoints(total_errors_404)
print('\nTop 5 endpoints causing error 404:')
for endpoint, count in top_five:
    print(endpoint, count)

# 404 errors per day
def daily_count(rdd):
    days = rdd.map(lambda line: line.split('[')[1].split(':')[0])
    counts = days.map(lambda day: (day, 1)).reduceByKey(add).collect()
    return counts

daily_counts = daily_count(total_errors_404)
print('\n404 errors per day:')
for day, count in daily_counts:
    print(day, count)

# Total byte count
def accumulated_byte_count(rdd):
    def byte_count(line):
        try:
            count = int(line.split(" ")[-1])
            if count < 0:
                raise ValueError()
            return count
        except:
            return 0
        
    count = rdd.map(byte_count).reduce(add)
    return count

print('Total byte count: %s' % accumulated_byte_count(dataset))
sc.stop()