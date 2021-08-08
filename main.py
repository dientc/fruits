from Reader import XAUDReader
from Ploter import Ploter
from Filter import Filter

fruits = []
weekday = []
    
def main():        
    fruits = XAUDReader().read('XAUUSD_Daily.csv')
    fruits.pop(0)   # remove header
    # print(fruits[0])

    weekday = Filter().zero(fruits)
    means = Filter().mean(fruits)
    Ploter().plotX(weekday, means)

if __name__ == "__main__":
    main()
