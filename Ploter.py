from datetime import datetime
from matplotlib import lines
import matplotlib.pyplot as plt

class Ploter:
    def __init__(self) -> None:
        pass
        
    def plot(self, fruits: list) -> None: 
        # x-axis values
        x = list(range(1, len(fruits) + 1))
        # y-axis values
        y = fruits
        
        # plotting points as a scatter plot
        plt.scatter(x, y, label= "stars", color= "black", 
                    marker= ".", s=5)
        
        # x-axis label
        plt.xlabel('x - Time')
        # frequency label
        plt.ylabel('y - USD')
        # plot title
        plt.title('Price error')
        # showing legend
        plt.legend()
        
        # function to show the plot
        plt.show()
            
    def plotX(self, fruits: list, means: list) -> None: 
        # x-axis values
        x = list(range(1, len(fruits) + 1))
        
        # y-axis values
        y = fruits
        y1 = means
        
        # plotting points as a scatter plot
        plt.scatter(x, y, label= "stars", color= "black", 
                    marker= ".", s=5)
        plt.plot(x, y1, label= "mean", color= "blue")
        # x-axis label
        plt.xlabel('x - Time')
        # frequency label
        plt.ylabel('y - USD')
        # plot title
        plt.title('Price error')
        # showing legend
        plt.legend()
        
        # function to show the plot
        plt.show()