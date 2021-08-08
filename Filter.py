from datetime import datetime

weekday = []

# print(toDate('2009.03.05'))
def toDate(strDate: str) -> datetime:
    date_time_obj = datetime.strptime(strDate, '%Y.%m.%d')

    return date_time_obj

class Filter:
    def __init__(self) -> None:
        pass

    def zero(self, fruits: list) -> list:  
        zeros = []
        for e in fruits:          
            dist = round(float(e[2]) - float(e[3]), 2) 
            # print(e[0], dist)
            zeros.append(dist)
        
        return zeros

    def mean(self, fruits: list) -> list:
        means = []
        for e in fruits:            
            dist = round((float(e[2]) + float(e[3]))/2, 2) 
            # print(e[0], dist)
            means.append(dist)
        
        return means

    def friday(self, fruits: list) -> list:
        for e in fruits:
            day = toDate(e[0])
            if  day.weekday() == 4:
                dist = round(float(e[2]) - float(e[3]), 2) 
                # print(e[0], dist)
                weekday.append(dist)
        
        return weekday