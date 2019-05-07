from kafka import SimpleProducer, KafkaClient
import requests
from dateutil.parser import parse
from datetime import datetime, timedelta
import time

def main():
    client = KafkaClient("localhost:9092")
    producer = SimpleProducer(client)

    last_hour = datetime.now() - timedelta(hours=1)
    print(last_hour)

    delim = '$$$$'

    time.sleep(20)
    # Dow Jones Industrial Average 30 stocks removed 3M
    stocks = ['American Express', 'Apple', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola', 'Walt Disney',
              'DowDuPont', 'ExxonMobil', 'General Electric', 'Goldman Sachs', 'The Home Depot', 'IBM', 'Intel',
              'Johnson & Johnson',
              'JPMorgan Chase', 'McDonald\'s', 'Merck', 'Microsoft', 'Nike', 'Pfizer', 'Procter & Gamble',
              'Travelers Companies',
              'United Technologies', 'UnitedHealth', 'Verizon', 'Visa', 'Wal-Mart']
    for stock in stocks:
        time.sleep(7)
        print('Stock being analyzed : ' + stock)
        #stock = stock.replace(" ", "%20")
        #stock = stock.replace("\'", "%2527")
        url = 'https://newsapi.org/v2/everything?q='+stock+'&apiKey=9714e1d74fb64495aaafdb54d4cdd0bc'
        response = requests.get(url)
        json_res = response.json()
        for post in json_res["articles"]:
            date_time = post["publishedAt"]
            #if parse(date_time).date() == last_hour.date() and parse(date_time).time() > last_hour.time():
            data= stock+delim+date_time
            if post["description"] is not None:
                data += delim + post["description"]
            else:
                continue
            if post["content"] is not None:
                data += " " + post["content"]
            msg = data.encode('utf-8')
            producer.send_messages(b'newsstream', msg)

if __name__ == '__main__':
    main()