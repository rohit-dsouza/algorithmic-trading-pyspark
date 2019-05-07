from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pyspark.sql.functions as F
import matplotlib.pyplot as plt
import nltk
import warnings
warnings.filterwarnings('ignore')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


def main():
    conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
    sc = SparkContext.getOrCreate(conf=conf)

    # Creating a streaming context with batch interval of 10 sec
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 10)
    ssc.checkpoint("checkpoint")
    pwords = load_wordlist("./Dataset/positive.txt")
    nwords = load_wordlist("./Dataset/negative.txt")
    stream(ssc, pwords, nwords, 300)

def load_wordlist(filename):
    """
    This function returns a list or set of words from the given filename.
    """
    words = {}
    f = open(filename, 'rU')
    text = f.read()
    text = text.split('\n')
    for line in text:
        words[line] = 1
    f.close()
    return words


def wordSentiment(word, pwords, nwords):
    if word in pwords:
        return ('positive', 1)
    elif word in nwords:
        return ('negative', 1)


def updateFunction(newValues, runningCount):
    if runningCount is None:
        runningCount = 0
    return sum(newValues, runningCount)


def sendRecord(record):
    connection = createNewConnection()
    connection.send(record)
    connection.close()


def stream(ssc, pwords, nwords, duration):
    delim = "$$$$"
    kstream = KafkaUtils.createDirectStream(ssc, topics=['newsstream'],
                                            kafkaParams={"metadata.broker.list": 'localhost:9092'})
    news = kstream.map(lambda x: x[1].encode("ascii", "ignore"))
    datardd = news.map(lambda x: x.split(delim)).map(lambda x: (x[0], x[1], sia.polarity_scores(x[2])['compound']))
    datardd.pprint()
    #df = datardd.toDF(["stock", "pubdate", "news"])
    '''
    # Each element of tweets will be the text of a tweet.
    # We keep track of a running total counts and print it at every time step.
    words = news.flatMap(lambda line: line.split(" "))
    positive = words.map(lambda word: ('Positive', 1) if word in pwords else ('Positive', 0))
    negative = words.map(lambda word: ('Negative', 1) if word in nwords else ('Negative', 0))
    allSentiments = positive.union(negative)
    sentimentCounts = allSentiments.reduceByKey(lambda x, y: x + y)
    runningSentimentCounts = sentimentCounts.updateStateByKey(updateFunction)
    runningSentimentCounts.pprint()

    # The counts variable hold the word counts for all time steps
    #counts = []
    #sentimentCounts.foreachRDD(lambda t, rdd: counts.append(rdd.collect()))
    '''
    # Start the computation
    ssc.start()
    ssc.awaitTerminationOrTimeout(duration)
    #ssc.awaitTermination()
    ssc.stop(stopGraceFully=True)

    #return counts


if __name__ == "__main__":
    main()
