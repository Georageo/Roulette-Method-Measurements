

def simulate(Unumbers):
    a=2.2
    s=3
    n=0
    LostCalls=0
    ParrivalList=[]
    PdepartureList=[]
    Service=[]
    State=[]
    TrunksList=[]
    Trunks=[0,0,0]
    for i in Unumbers:
        if n==0:
            n=1
            Parrival=1
            Pdeparture=0
            ParrivalList.append(Parrival)
            PdepartureList.append(Pdeparture)
            Service.append("YES")
            State.append("Arrival")
            Trunks[0]=1
            TrunksList.append(Trunks.copy())
        
        else:
            Parrival=a/(a+n)
            Pdeparture=n/(a+n)
            if i <= Parrival:
                if Trunks[2]==1:
            
                    LostCalls=LostCalls+1
                    ParrivalList.append(0)
                    PdepartureList.append(0)
                    Service.append("NO")
                    State.append("Loss")
                    TrunksList.append(Trunks.copy())
                else:

                    n=n+1
                    ParrivalList.append(Parrival)
                    PdepartureList.append(Pdeparture)
                    Service.append("YES")
                    State.append("Arrival")
                    if Trunks[1]==1:
                        Trunks[2]=1
                    else:
                        Trunks[1]=1
                    TrunksList.append(Trunks.copy())
            else:
                n=n-1
                ParrivalList.append(Parrival)
                PdepartureList.append(Pdeparture)
                Service.append("YES")
                State.append("Departure")
                if Trunks[2]==1:
                    Trunks[2]=0
                elif Trunks[2]==0 and Trunks[1]==1:
                    Trunks[1]=0
                elif Trunks[2]==0 and Trunks[0]==1 and Trunks[0]==1:
                    Trunks[0]=0
                TrunksList.append(Trunks.copy())
        
    

    return ParrivalList, PdepartureList, TrunksList, State, Service,LostCalls



