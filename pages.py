import csv
from turtle import color
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

class Process:
    def __init__(self, processID, switchNo, activePages, shares = 1000000000, pagesAllocated = 1000000000) -> None:
        self.processID = processID
        self.switchNo = switchNo
        self.activePages = activePages
        self.shares = shares
        self.pagesAllocated = pagesAllocated
        self.cost = -1

    def calcCost(self, tax):
        k = 1/(1-tax)
        f = self.activePages/self.pagesAllocated
        self.cost = self.shares/(self.pagesAllocated * (f + k *(1-f)))
    
    def mergeProcess(self, p):
        self.processID = p.processID
        self.activePages = self.activePages + p.activePages

    def printProcess(self) -> None:
        print("Process ID: " + str(self.processID) + "\tCost: " + str(self.cost))
    

class Processor:
    def __init__(self, limit = 5, tax = 0.75) -> None:
        self.processes = []
        self.total = []
        self.limit = limit
        self.tax = tax

    def addProcess(self, p) -> None:
        for i in self.processes:
            if i.switchNo == p.switchNo:
                i.mergeProcess(p)
                i.calcCost(self.tax)
                self.calcTotal()
                return
        if len(self.processes) == self.limit:
            self.removeProcess()
        p.calcCost(self.tax)
        self.processes.append(p)
        self.calcTotal()

    def addProcessDefault(self, p) -> None:
        for i in self.processes:
            if i.switchNo == p.switchNo:
                i.mergeProcess(p)
                i.calcCost(self.tax)
                self.calcTotal()
                return
        if len(self.processes) == self.limit:
            self.processes.pop(0)
        p.calcCost(self.tax)
        self.processes.append(p)
        self.calcTotal()
    
    def addProcessAccurate(self, p) -> None:
        for i in self.processes:
            if i.switchNo == p.switchNo:
                i.mergeProcess(p)
                i.calcCost(self.tax)
                self.calcTotal()
                return
        if len(self.processes) == 20:
            self.processes.pop(0)
        p.calcCost(self.tax)
        self.processes.append(p)
        self.calcTotal()

    def removeProcess(self) -> None:
        if len(self.processes) > 0:
            i = 0
            minCost = self.processes[0].cost
            for x in range(len(self.processes)):
                if self.processes[x].cost < minCost:
                    minCost = self.processes[x].cost
                    i = x
            self.processes.pop(i)

    def calcTotal(self):
        i = 0
        for x in self.processes:
            i = i  + x.activePages
        self.total.append(i)
    
    def printState(self) -> None:
        print("\nProcesses: ")
        for p in self.processes:
            p.printProcess()
        print(self.total)

def main():
    #Create processor
    #Optional arguments: max number of processors (default 5), Tax (default 0.75)
    P = Processor()
    P2 = Processor()
    accurateTransfer = Processor()

    file = open('temp.csv')
    csvreader = csv.reader(file)
    # header = []
    # header = next(csvreader)

    rows = []
    for row in csvreader:
        P.addProcess(Process(int(row[0]), int(row[1]), int(row[2])))
        P2.addProcessDefault(Process(int(row[0]), int(row[1]), int(row[2])))
        accurateTransfer.addProcessAccurate(Process(int(row[0]), int(row[1]), int(row[2])))
        # P.printState()

    y1 = P.total
    x1 = [i for i in range(len(y1))]
    # plt.plot(x1, y1, label = "line 1")

    y2 = P2.total
    x2 = [i for i in range(len(y2))]

    y2 = np.array(y2)
    x2 = np.array(x2)
    X_Y_Spline = make_interp_spline(x2, y2)
 
    X_ = np.linspace(x2.min(), x2.max(), 500)
    Y_ = X_Y_Spline(X_)

    y3 = accurateTransfer.total
    x3 = [i for i in range(len(y3))]


    figure, axis = plt.subplots(1, 3)

    axis[0].plot(x1, y1, label = "min funding revocation algorithm",color = "red")
    
    axis[1].plot(X_, Y_, label = "original first removal algorithm", color = "black")
    axis[2].plot(x3, y3, label = "accurate data transfer considering")
    figure.set_xlabel = ("Time")
    figure.set_ylabel = ("Number of Packets Sent")

    plt.legend()
    plt.show()
    

    

if __name__ == "__main__":  
    main()

