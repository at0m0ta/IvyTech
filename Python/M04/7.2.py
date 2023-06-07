'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 7.2
    
    02/10/2018
    
    '''
# 7.2 The stock class

class Stock:
    def __init__(self, name, symbol, previousPrice, currentPrice):  #initiating objects
        self.__name = name
        self.__symbol = symbol
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice

    def getInfo(self):                                              #collects information from self object
        return self.__name 
        return self.__symbol
        return self.__previousPrice
        return self.__currentPrice

    def setPreviousPrice(self, previousPrice):                      #setting the current and previous prices
        self.__previousPrice = previousPrice
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):                                     #getting the percentage and formatting decimal
        return format((self.__currentPrice - self.__previousPrice) * 100 / self.__previousPrice, "5.2f") + "%"

def main():
    stock = Stock("Intel", "INTC", 20.5, 20.35)                     #printing the pricechange percentage
    print("The price change is " + str(stock.getChangePercent()))
          
main()
