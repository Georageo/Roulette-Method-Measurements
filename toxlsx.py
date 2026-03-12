import pandas as pd
import main

def toexcel(x0,numbers,Unumbers,Parrival,Pdeparture,State,Trunks,Service,Ploss):
    no= list(range(1, 33))
    df=pd.DataFrame({
        'No': no,
        'Random':numbers,
        'U-number':Unumbers,
        'P(arrival)':Parrival,
        'P(departure)':Pdeparture,
        'State':State,
        'Trunks': Trunks,
        'Service': Service
        

    })

    excel_filename = f"results_seed_{x0}.xlsx"
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
       
        pd.DataFrame([['Simulation with seed number : ',x0,'Ploss: ',Ploss]]).to_excel(writer, index=False, header=False, startrow=0)
        
        df.to_excel(writer, index=False, startrow=1)

    