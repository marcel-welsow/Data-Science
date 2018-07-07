from pyspark import SparkContext

sc = SparkContext("local", "PythonWordCountSorted")

text_file = sc.textFile("t8.shakespeare.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b)

output = counts.map(lambda (a, b): (b, a)).sortByKey(False).take(24)

for (count, word) in output:
    print(count + " found the word" + word)
