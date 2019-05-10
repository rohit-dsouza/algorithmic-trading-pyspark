from kafka import SimpleProducer, KafkaClient
import requests
from dateutil.parser import parse
from datetime import datetime, timedelta
import time
import csv
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    time.sleep(40)
    makeStream()
    scheduler = BlockingScheduler()
    scheduler.add_job(makeStream, 'interval', hours=1)
    scheduler.start()


def makeStream():
    client = KafkaClient("localhost:9092")
    producer = SimpleProducer(client)

    with open('test1.txt', 'r') as file:
        filedata = file.read().replace('\n', '')
        text = filedata.split("-----------------------------------------------")
        for data in text:
            msg = data.encode('utf-8')
            producer.send_messages(b'newsstream', msg)


    """
    #stocks = getStocks()
    stocks = ['NYSE: MMM', 'NYSE: AXP', 'NASDAQ: AAPL', 'NYSE: BA', 'NYSE: CAT', 'NYSE: CVX', 'NASDAQ: CSCO', 'NYSE: KO',
             'NYSE: DIS', 'NYSE: DOW', 'NYSE: XOM', 'NYSE: GS', 'NYSE: HD', 'NYSE: IBM', 'NASDAQ: INTC', 'NYSE: JNJ',
             'NYSE: JPM', 'NYSE: MCD', 'NYSE: MRK', 'NASDAQ: MSFT', 'NYSE: NKE', 'NYSE: PFE', 'NYSE: PG', 'NYSE: TRV',
             'NYSE: UTX', 'NYSE: UNH', 'NYSE: VZ', 'NYSE: V', 'NYSE: WMT', 'NASDAQ: WBA']

    delim = '$$$$'

    for stock in stocks[0:1]:
        time.sleep(7)
        yesterday = datetime.now() - timedelta(days=5)
        print('Stock being analyzed : ' + stock)
        cx = '017984621812319695223:8lygbaavsbi'
        key = 'AIzaSyAKj1glFOvmqUbCdOtXOi6yOvRJ-alUFT0'
        url = 'https://www.googleapis.com/customsearch/v1?key='+key+'&cx='+cx+'&q='+stock
        response = requests.get(url)
        json_res = response.json()
        print(json_res)
        if 'items' in json_res and len(json_res['items']) != 0:
            for item in json_res['items']:
                if 'pagemap' in item and 'newsarticle' in item['pagemap']:
                    for article in item['pagemap']['newsarticle']:
                        datePublished = article['datepublished']
                        if parse(datePublished).date() >= yesterday.date():
                            print(article['description'])
                            temp = stock.split(": ")
                            content = temp[0] + delim + temp[1] + delim + datePublished
                            if 'description' in article:
                                content += delim + article['description']
                                if 'articlebody' in article:
                                    content += " " + article['articlebody']
                            msg = content.encode('utf-8')
                            producer.send_messages(b'newsstream', msg)
    """

def getStocks():

    markets = {'NASDAQ': 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download',
        'NYSE': 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download'}
    stocks = []
    with requests.Session() as s:
        for market in markets:
            download = s.get(markets[market])
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list[1:]:
                stock = market+': '+row[0].replace("^", "-")
                stocks.append(stock)
    return stocks

if __name__ == '__main__':
    main()