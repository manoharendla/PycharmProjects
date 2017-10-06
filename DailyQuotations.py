__author__ = '619635'
import random

quoteanddate={1:"Instead of using our intelligence on why a thing can't be done, let us use it to find out how it can be done",2:"Make your potential count. Seek most and more from life. Seek abundance.",}
def getQuote(date):
      print("Quote for the day"+str(date),quoteanddate.__getitem__(date))

date=random.randint(1,2)
fortune=getQuote(date)




