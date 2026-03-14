import NumberGenerator
import simulation
import toxlsx
import plotcreation

def main():
    numbers, Unumbers, x0 = NumberGenerator.run_generator()
    ParrivalList1, PdepartureList1, TrunksList, State, Service, LostCalls = simulation.simulate(Unumbers)
    ParrivalList=[round(x,3) for x in ParrivalList1]
    PdepartureList=[round(x,3) for x in PdepartureList1]
    Ploss=round(LostCalls/(32-LostCalls),4)
    toxlsx.toexcel(x0,numbers,Unumbers,ParrivalList,PdepartureList,State,TrunksList,Service,Ploss)
    print("Data have been saved")
    plotcreation.create_plot()

if __name__ == "__main__":
    main()

