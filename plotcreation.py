import pandas as pd
import matplotlib.pyplot as plt
import glob 


def create_plot():
    seeds=[]
    Ploss=[]
    files = glob.glob("results*.xlsx")
    for file in files:
        df = pd.read_excel(file, header=None)

        x = df.iloc[0,1]   
        y = df.iloc[0,3]   

        seeds.append(x)
        Ploss.append(y)
    points = sorted(zip(seeds,Ploss))
    x_sorted, y_sorted = zip(*points)
    plt.plot(x_sorted, y_sorted, marker='o')
    plt.xlabel("Seed Numbers")
    plt.ylabel("'%' of Losses")
    plt.title("Blocking=f(x0)")
    plt.savefig("plot.png")
    print("Plot has been updated") 
    plt.show()