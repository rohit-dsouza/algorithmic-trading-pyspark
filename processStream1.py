from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import nltk
import warnings
import pymongo_spark
warnings.filterwarnings('ignore')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def main():

    pymongo_spark.activate()
    conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
    sc = SparkContext.getOrCreate(conf=conf)

    # Creating a streaming context with batch interval of 10 sec
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 10)
    ssc.checkpoint("checkpoint")
    stream(ssc, 300)


def stream(ssc, duration):

    delim = "$$$$"
    kstream = KafkaUtils.createDirectStream(ssc, topics=['newsstream'],
                                            kafkaParams={"metadata.broker.list": 'localhost:9092'})
    news = kstream.map(lambda x: x[1].encode("ascii", "ignore"))

    # Market    Symbol  Date_Published  Sentiment
    datardd = news.map(lambda x: x.split(delim)).map(lambda x: (x[0], x[1], x[2], sia.polarity_scores(x[3])['compound']))

    """
    requestsDataFrame = datardd.map(lambda w: Row(
        str(w._1), str(w._2), str(w._2), str(w._3)))
    """

    datardd.foreachRDD(lambda rdd : savetoDB(rdd))

    # Start the computation
    ssc.start()
    #ssc.awaitTerminationOrTimeout(duration)
    ssc.awaitTermination()
    ssc.stop(stopGraceFully=True)

def savetoDB(rdd):
    if not rdd.isEmpty():
        rdd.saveToMongoDB('mongodb://localhost:27017/stocksdb.stockscol')

if __name__ == "__main__":
    main()
