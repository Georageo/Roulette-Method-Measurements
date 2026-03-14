import pandas as pd
import matplotlib.pyplot as plt
import glob 


def create_plot():
    seeds=[]
    Ploss=[]
    files = glob.glob("results*.xlsx")
    for file in files:
        df = pd.read_excel(file, header=None)

        x = 2.2   
        y = df.iloc[0,3]   

        seeds.append(x)
        Ploss.append(y)
    points = sorted(zip(seeds,Ploss))
    x_sorted, y_sorted = zip(*points)
    plt.plot(x_sorted, y_sorted, marker='o')
    plt.axhline(y=0.24, color='red', linestyle='--', label='Ε3(2.2) = 24%')
    plt.xlabel("Traffic Load (Erlang)")
    plt.ylabel("'%' of Losses")
    plt.title("Blocking")
    plt.legend()
    plt.savefig("plot.png")
    print("Plot has been updated") 
    plt.show()