import random
import csv
def Stadium():
    # Take the Stadium Input From user and return it to main
    Std=input("Enter the Name of Stadium : ")
    return Std
def FirstTeam():
    Frst=input("Enter First Team Name : ")
    return Frst
def limit(Team):
    if Team=="RCB":
        return 1
    elif Team=="CSK":
        return 23
    elif Team=="DC":
        return 112
    elif Team=="KKR":
        return 48
    elif Team=="MI":
        return 69
    elif Team=="PBKS":
        return 154
    elif Team=="RR":
        return 92
    elif Team=="SRH":
        return 134
def uplimit(Team):
    if Team=="RCB":
        return 22
    elif Team=="CSK":
        return 47
    elif Team=="DC":
        return 133
    elif Team=="KKR":
        return 68
    elif Team=="MI":
        return 91
    elif Team=="PBKS":
        return 178
    elif Team=="RR":
        return 111
    elif Team=="SRH":
        return 153
def Show(Team):
    column_list = []
    column_lis=[]
    column_li=[]
    if Team=="RCB":
        csfile="RCB.csv"
    elif Team=="CSK":
        csfile="CSK.csv"
    elif Team=="DC":
        csfile="DC.csv"
    elif Team=="KKR":
        csfile="KKR.CSV"
    elif Team=="MI":
        csfile="MI.csv"
    elif Team=="PBKS":
        csfile="PBKS.csv"
    elif Team=="RR":
        csfile="RR.csv"
    elif Team=="SRH":
        csfile="SRH.csv"
    with open(csfile, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['\ufeffBatter']!="":
                column_list.append(row['\ufeffBatter'])
            if row['All Rounders']!="":
                column_lis.append(row['All Rounders'])
            if row['Bowlers']!="":
                column_li.append(row['Bowlers'])
    print("Batter : ")
    for i in column_list:
        print(i)
    print("All Rounders : ")
    for i in column_lis:
        print(i)
    print("Bowlers : ")
    for i in column_li:
        print(i)
def SecondTeam():
    Sec=input("Enter Second Team Name : ")
    return Sec
class Player:
    def __init__(self):
        self.Name=""
        self.Runs=0
        self.Bowls=0
        self.fours=0
        self.sixes=0
        self.Runrate=0
        self.Overs=0
        self.RunOvr=0
        self.Wickets=0
        self.Economy=0
        self.Out=""
def NameofPlayer(Serial,Team):
    Jersey=input(f"Enter the Jersey No. of {Serial} Player of {Team} Team :")
    return Jersey
def Toss():
    tos=input("Press 'T' for Toss : ")
    return tos
def decision():
    dec=input("Choose Bat or Bowl : ")
    return dec
def Start():
    begin=input("Press 'S' to start the match : ")
    return begin
def play():
    ply=input("Press 'P' to Play the Ball : ")
    return ply
def cont():
    Play=""
    while Play!="P":
        Play=play()
        if Play!="P":
            print("Invalid Input")
def Strikerf():
    ser=input("Enter the serial number of the Player : ")
    return ser
def Output(Stadium):
    choicess=["0","1","2","4","6","W"]
    if Stadium=='Wankhade':
        probablity=[0.277874,0.378316,0.094579,0.130046,0.068435,0.05075]
    elif Stadium=='M A Chidambaran':
        probablity=[0.384228,0.319597,0.079899,0.11177,0.049659,0.054847]
    elif Stadium=='Arun Jaitley':
        probablity=[0.24947,0.384127,0.096032,0.140212,0.079101,0.051058]
    elif Stadium=='Eden Gardens' or 'PCA Mohali':
        probablity=[0.245772,0.377523,0.094381,0.141844,0.087834,0.052646]
    elif Stadium=='SMS':
        probablity=[0.240789,0.421053,0.105263,0.125,0.061842,0.046053]
    elif Stadium=='M Chinaswamy':
        probablity=[0.232066,0.398529,0.099632,0.127529,0.08737,0.054874]
    elif Stadium=='Rajiv Gandhi':
        probablity=[0.246684,0.397878,0.099469,0.136605,0.071618,0.047746]
    outcome=random.choices(choicess, weights=probablity, k=1)[0]
    return outcome
def Out():
    foices=["Caught Out","Bowled Out","Run Out","Stumped Out","LBW Out"]
    prob=[0.50,0.30,0.10,0.02,0.08]
    outcomeee=random.choices(foices,weights=prob,k=1)[0]
    return outcomeee
def Choosestr1(Inn,ser):
    inp=input(f"Press C to Choose the Striker {ser} of {Inn} Team: ")
    return inp
def ChooseNew(Inn,wic):
    inp=input(f"Press C to Choose the {wic+2}th Batter of {Inn} Team : ")
    return inp
def ChooseBowl(Inn):
    inp=input(f"Press C to Choose Bowler of {Inn} Team : ")
    return inp
def PrintStat():
    inp=input(f"Press P to Print the Summary of the match : ")
    return inp
stadium=""
StadiumList=["Wankhade","M A Chidambaran","Arun Jaitley","Eden Gardens","PCA Mohali","SMS","M Chinaswamy","Rajiv Gandhi"]
while stadium not in StadiumList:
    stadium=Stadium()
    if stadium not in StadiumList:
        print("Sorry Only following Stadium is available for now!")
        for i in StadiumList:
            print(i,end=", ")
        print()
overs=20
firstTeam=""
TeamList=["RCB","CSK","DC","PBKS","KKR","SRH","RR","MI"]
while firstTeam not in TeamList:
    firstTeam=FirstTeam()
    if firstTeam not in TeamList:
        print("Sorry Only following Team are available for now!")
        for i in TeamList:
            print(i,end=", ")
        print()
player1=Player()
player2=Player()
player3=Player()
player4=Player()
player5=Player()
player6=Player()
player7=Player()
player8=Player()
player9=Player()
player10=Player()
player11=Player()
Players1=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
a=1
Show(firstTeam)
Play_Jersey = []
with open('List.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
            Play_Jersey.append(row['\ufeffPlayer Name'])
lo=limit(firstTeam)
hi=uplimit(firstTeam)
repetition=[]
for i in Players1:
    jersey=-1
    while jersey<lo or jersey>hi or jersey in repetition:
        try:
            jersey=int(NameofPlayer(f"{a}th",firstTeam))
            if jersey<lo or jersey>hi or jersey in repetition:
                print("Invalid Jersey No.!")
        except ValueError:
            print("Invalid Jersey No.!")
    repetition.append(jersey)
    i.Name=Play_Jersey[jersey-1]
    a+=1
print("First Team Players : ")
for i in Players1:
    print(i.Name)
secondTeam=""
while secondTeam not in TeamList or secondTeam==firstTeam:
    secondTeam=SecondTeam()
    if secondTeam not in TeamList:
        print("Sorry Only following Team are available for now!")
        for i in TeamList:
            print(i,end=", ")
        print()
    elif secondTeam==firstTeam:
        print("Second Team cannot be equal to first Team")
Player1=Player()
Player2=Player()
Player3=Player()
Player4=Player()
Player5=Player()
Player6=Player()
Player7=Player()
Player8=Player()
Player9=Player()
Player10=Player()
Player11=Player()
Players2=[Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11]
a=1
Show(secondTeam)
lo=limit(secondTeam)
hi=uplimit(secondTeam)
repetiton=[]
for i in Players2:
    jersey=-1
    while jersey<lo or jersey>hi or jersey in repetiton:
        try:
            jersey=int(NameofPlayer(f"{a}th",secondTeam))
            if jersey<lo or jersey>hi or jersey in repetiton:
                print("Invalid Jersey No.!")
        except ValueError:
            print("Invalid Jersey No.!")
    repetiton.append(jersey)
    i.Name=Play_Jersey[jersey-1]
    a+=1
print("Second Team Players : ")
for i in Players2:
    print(i.Name)
toss=""
while toss!="T":
    toss=Toss()
    if toss!="T":
        print("Invalid Input")
choice=[firstTeam,secondTeam]
probablities=[0.5,0.5]
outcomes=random.choices(choice, weights=probablities, k=1)[0]
TossWin=outcomes
Tosslose=""
if(TossWin==firstTeam):
    Tosslose=secondTeam
else:
    Tosslose=firstTeam
print(f"{TossWin} won the Toss")
Decision=""
while Decision!="Bat" and Decision!="Bowl":
    Decision=decision()
    if Decision!="Bat" and Decision!="Bowl":
        print("Invalid Input")
begin=""
while begin!="S":
    begin=Start()
    if begin!="S":
        print("Invalid Input")
totalruns=0
wickets=0
over=0
Inn1=TossWin
if Decision!="Bat":
    Inn1=Tosslose
strike1=""
strike2=""
strikeb=""
if Inn1==firstTeam:
    striker1=""
    while striker1!='C':
        striker1=Choosestr1(Inn1,1)
        if striker1!='C':
            print("Invalid Input")
    x=1
    for i in Players1:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<1 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<1 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike1=Players1[serial-1]
    temp=Players1[serial-1]
    Players1[serial-1]=Players1[0]
    Players1[0]=temp
    striker2=""
    while striker2!='C':
        striker2=Choosestr1(Inn1,2)
        if striker2!='C':
            print("Invalid Input")
    x=1
    for i in Players1:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<2 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<2 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike2=Players1[serial-1]
    temp=Players1[serial-1]
    Players1[serial-1]=Players1[1]
    Players1[1]=temp
else:
    striker1=""
    while striker1!='C':
        striker1=Choosestr1(Inn1,1)
        if striker1!='C':
            print("Invalid Input")
    x=1
    for i in Players2:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<1 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<1 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike1=Players2[serial-1]
    temp=Players2[serial-1]
    Players2[serial-1]=Players2[0]
    Players2[0]=temp
    striker2=""
    while striker2!='C':
        striker2=Choosestr1(Inn1,2)
        if striker2!='C':
            print("Invalid Input")
    x=1
    for i in Players2:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<2 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<2 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike2=Players2[serial-1]
    temp=Players2[serial-1]
    Players2[serial-1]=Players2[1]
    Players2[1]=temp
strikeb=Players1[0]
strikeb.Overs-=1
strike=strike2
flag=True
for i in range(1,overs+1):
    strikeb.Overs+=1
    if strikeb.RunOvr==0 or strikeb.Overs==0:
        strikeb.Economy=0
    else:
        strikeb.Economy=int(strikeb.RunOvr/strikeb.Overs)
    if flag==False:
        print("All Out!")
        break
    over=i-1
    if strike==strike1:
        strike=strike2
    else:
        strike=strike1
    if Inn1==firstTeam:
        chooseb=""
        while chooseb!='C':
            chooseb=ChooseBowl(secondTeam)
            if chooseb!='C':
                print("Invalid Input!")
        x=1
        for i in Players2:
            print(x,end=" : ")
            print(i.Name)
            x+=1
        serial=-1
        while serial<1 or serial>11 or Players2[serial-1].Overs>3 or Players2[serial-1]==strikeb:
            try:
                serial=int(Strikerf())
                if serial<1 or serial>11 or Players2[serial-1].Overs>3 or Players2[serial-1]==strikeb:
                    print("Enter valid serial No.!")
            except ValueError:
                print("Enter valid serial No.!")
        strikeb=Players2[serial-1]
    else:
        chooseb=""
        while chooseb!='C':
            chooseb=ChooseBowl(firstTeam)
            if chooseb!='C':
                print("Invalid Input!")
        x=1
        for i in Players1:
            print(x,end=" : ")
            print(i.Name)
            x+=1
        serial=-1
        while serial<1 or serial>11 or Players1[serial-1].Overs>3 or Players1[serial-1]==strikeb:
            try:
                serial=int(Strikerf())
                if serial<1 or serial>11 or Players1[serial-1].Overs>3 or Players1[serial-1]==strikeb:
                    print("Enter valid serial No.!")
            except ValueError:
                print("Enter valid serial No.!")
        strikeb=Players1[serial-1]
    for j in range(1,7):
        if flag==False:
            break
        cont()
        Outp=Output(stadium)
        if(Outp!="W"):
            totalruns+=int(Outp)
            strike.Runs+=int(Outp)
            strike.Bowls+=1
            strikeb.RunOvr+=int(Outp)
            if Outp=='4':
                strike.fours+=1
            elif Outp=='6':
                strike.sixes+=1
            elif Outp=='1' or Outp=='3':
                if strike==strike1:
                    strike=strike2
                else:
                    strike=strike1
        else: 
            strike.Bowls+=1
            wickets+=1
            strikeb.Wickets+=1
            if wickets==10:
                print("All Out")
                flag=False
            else:
                ruledout=Out()
                strike.Out=ruledout+" by "+strikeb.Name
                print(f"{strike.Name} {ruledout} by {strikeb.Name}!")
                choosen=""
                while choosen!='C':
                    choosen=ChooseNew(Inn1,wickets)
                    if choosen!='C':
                        print("Invalid Input!")
                if Inn1==firstTeam:
                    x=1
                    for i in Players1:
                        print(x,end=" : ")
                        print(i.Name)
                        x+=1
                    if strike==strike1:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike1=Players1[serial-1]
                        temp=Players1[serial-1]
                        Players1[serial-1]=Players1[wickets+1]
                        Players1[wickets+1]=temp
                        strike=strike1
                    else:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike2=Players1[serial-1]
                        temp=Players1[serial-1]
                        Players1[serial-1]=Players1[wickets+1]
                        Players1[wickets+1]=temp
                        strike=strike2
                else:
                    x=1
                    for i in Players2:
                        print(x,end=" : ")
                        print(i.Name)
                        x+=1
                    if strike==strike1:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike1=Players2[serial-1]
                        temp=Players2[serial-1]
                        Players2[serial-1]=Players2[wickets+1]
                        Players2[wickets+1]=temp
                        strike=strike1
                    else:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike2=Players2[serial-1]
                        temp=Players2[serial-1]
                        Players2[serial-1]=Players2[wickets+1]
                        Players2[wickets+1]=temp
                        strike=strike2
        if strike1.Runs==0 or strike1.Bowls==0:
            strike1.Runrate=0
        else:
            strike1.Runrate=int((strike1.Runs/strike1.Bowls)*100)
        if strike2.Runs==0 or strike2.Bowls==0:
            strike2.Runrate=0
        else:
            strike2.Runrate=int((strike2.Runs/strike2.Bowls)*100)
        if totalruns==0:
            crr=0
        else:
            crr=(totalruns/((over*6)+j))*6
            crr=round(crr,2)
        print(Inn1)
        print(f"{totalruns}/{wickets}")
        print(f"({over}.{j})")
        print(f"             R   B   4s  6s  S/R")
        if strike==strike1:
            print("*",end="")
        print(f"{strike1.Name} : {strike1.Runs} {strike1.Bowls} {strike1.fours} {strike1.sixes} {strike1.Runrate}")
        if strike==strike2:
            print("*",end="")
        print(f"{strike2.Name} : {strike2.Runs} {strike2.Bowls} {strike2.fours} {strike2.sixes} {strike2.Runrate}")
        print(f"CRR : {crr}")
        print(f"{strikeb.Name} : {strikeb.Wickets}/{strikeb.RunOvr}({strikeb.Overs}.{j})")
        print(Outp)
target=totalruns
Fwickets=wickets
Fover=over
Fball=j
begin=""
while begin!="S":
    begin=Start()
    if begin!="S":
        print("Invalid Input")
totalruns=0
wickets=0
over=0
if Inn1==firstTeam:
    Inn2=secondTeam
else:
    Inn2=firstTeam
strike1=""
strike2=""
if Inn2==firstTeam:
    striker1=""
    while striker1!='C':
        striker1=Choosestr1(Inn2,1)
        if striker1!='C':
            print("Invalid Input")
    x=1
    for i in Players1:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<1 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<1 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike1=Players1[serial-1]
    temp=Players1[serial-1]
    Players1[serial-1]=Players1[0]
    Players1[0]=temp
    striker2=""
    while striker2!='C':
        striker2=Choosestr1(Inn2,2)
        if striker2!='C':
            print("Invalid Input")
    x=1
    for i in Players1:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<2 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<2 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike2=Players1[serial-1]
    temp=Players1[serial-1]
    Players1[serial-1]=Players1[1]
    Players1[1]=temp
else:
    striker1=""
    while striker1!='C':
        striker1=Choosestr1(Inn2,1)
        if striker1!='C':
            print("Invalid Input")
    x=1
    for i in Players2:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<1 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<1 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike1=Players2[serial-1]
    temp=Players2[serial-1]
    Players2[serial-1]=Players2[0]
    Players2[0]=temp
    striker2=""
    while striker2!='C':
        striker2=Choosestr1(Inn2,2)
        if striker2!='C':
            print("Invalid Input")
    x=1
    for i in Players2:
        print(x,end=" : ")
        print(i.Name)
        x+=1
    serial=-1
    while serial<2 or serial>11:
        try:
            serial=int(Strikerf())
            if serial<2 or serial>11:
                print("Enter valid serial No.!")
        except ValueError:
            print("Enter valid serial No.!")
    strike2=Players2[serial-1]
    temp=Players2[serial-1]
    Players2[serial-1]=Players2[1]
    Players2[1]=temp
strikeb=Players1[0]
strikeb.Overs-=1
strike=strike2
flag=True
win=False
for i in range(1,overs+1):
    strikeb.Overs+=1
    if strikeb.RunOvr==0 or strikeb.Overs==0:
        strikeb.Economy=0
    else:
        strikeb.Economy=int(strikeb.RunOvr/strikeb.Overs)
    if flag==False:
        print("All Out!")
        break
    if win==True:
        break
    if totalruns>target:
        win=True
        print(f"{Inn2} Wins by {10-wickets} Wickets!")
        break
    over=i-1
    if strike==strike1:
        strike=strike2
    else:
        strike=strike1
    if Inn2==firstTeam:
        chooseb=""
        while chooseb!='C':
            chooseb=ChooseBowl(secondTeam)
            if chooseb!='C':
                print("Invalid Input!")
        x=1
        for i in Players2:
            print(x,end=" : ")
            print(i.Name)
            x+=1
        serial=-1
        while serial<1 or serial>11 or Players2[serial-1].Overs>3 or Players2[serial-1]==strikeb:
            try:
                serial=int(Strikerf())
                if serial<1 or serial>11 or Players2[serial-1].Overs>3 or Players2[serial-1]==strikeb:
                    print("Enter valid serial No.!")
            except ValueError:
                print("Enter valid serial No.!")
        strikeb=Players2[serial-1]
    else:
        chooseb=""
        while chooseb!='C':
            chooseb=ChooseBowl(firstTeam)
            if chooseb!='C':
                print("Invalid Input!")
        x=1
        for i in Players1:
            print(x,end=" : ")
            print(i.Name)
            x+=1
        serial=-1
        while serial<1 or serial>11 or Players1[serial-1].Overs>3 or Players1[serial-1]==strikeb:
            try:
                serial=int(Strikerf())
                if serial<1 or serial>11 or Players1[serial-1].Overs>3 or Players1[serial-1]==strikeb:
                    print("Enter valid serial No.!")
            except ValueError:
                print("Enter valid serial No.!")
        strikeb=Players1[serial-1]
    for j in range(1,7):
        if flag==False:
            break
        if totalruns>target:
            win=True
            print(f"{Inn2} Wins by {10-wickets} Wickets!")
            j-=1
            break
        cont()
        Outp=Output(stadium)
        if(Outp!="W"):
            totalruns+=int(Outp)
            strike.Runs+=int(Outp)
            strike.Bowls+=1
            strikeb.RunOvr+=int(Outp)
            if Outp=='4':
                strike.fours+=1
            elif Outp=='6':
                strike.sixes+=1
            elif Outp=='1' or Outp=='3':
                if strike==strike1:
                    strike=strike2
                else:
                    strike=strike1
        else: 
            strike.Bowls+=1
            wickets+=1
            strikeb.Wickets+=1
            if wickets==10:
                print("All Out")
                flag=False
            else:
                ruleout=Out()
                strike.Out=ruleout+" by "+strikeb.Name
                print(f"{strike.Name} {ruleout} by {strikeb.Name}!")
                choosen=""
                while choosen!='C':
                    choosen=ChooseNew(Inn2,wickets)
                    if choosen!='C':
                        print("Invalid Input!")
                if Inn2==firstTeam:
                    x=1
                    for i in Players1:
                        print(x,end=" : ")
                        print(i.Name)
                        x+=1
                    if strike==strike1:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike1=Players1[serial-1]
                        temp=Players1[serial-1]
                        Players1[serial-1]=Players1[wickets+1]
                        Players1[wickets+1]=temp
                        strike=strike1
                    else:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike2=Players1[serial-1]
                        temp=Players1[serial-1]
                        Players1[serial-1]=Players1[wickets+1]
                        Players1[wickets+1]=temp
                        strike=strike2
                else:
                    x=1
                    for i in Players2:
                        print(x,end=" : ")
                        print(i.Name)
                        x+=1
                    if strike==strike1:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike1=Players2[serial-1]
                        temp=Players2[serial-1]
                        Players2[serial-1]=Players2[wickets+1]
                        Players2[wickets+1]=temp
                        strike=strike1
                    else:
                        serial=-1
                        while serial<(wickets+2) or serial>11:
                            try:
                                serial=int(Strikerf())
                                if serial<(wickets+2) or serial>11:
                                    print("Enter valid serial No.!")
                            except ValueError:
                                print("Enter valid serial No.!")
                        strike2=Players2[serial-1]
                        temp=Players2[serial-1]
                        Players2[serial-1]=Players2[wickets+1]
                        Players2[wickets+1]=temp
                        strike=strike2
        if strike1.Runs==0 or strike1.Bowls==0:
            strike1.Runrate=0
        else:
            strike1.Runrate=int((strike1.Runs/strike1.Bowls)*100)
        if strike2.Runs==0 or strike2.Bowls==0:
            strike2.Runrate=0
        else:
            strike2.Runrate=int((strike2.Runs/strike2.Bowls)*100)
        if totalruns==0:
            crr=0
        else:
            crr=(totalruns/((over*6)+j))*6
            crr=round(crr,2)
        if target==totalruns or ((overs*6)-((over*6)+j))==0 or (target-totalruns)<=0:
            rrr=0
        else:
            rrr=((target-totalruns)/((overs*6)-((over*6)+j)))*6
            rrr=round(rrr,2)
        print(Inn2)
        print(f"{totalruns}/{wickets}")
        print(f"({over}.{j})")
        print(f"             R   B   4s  6s  S/R")
        if strike==strike1:
            print("*",end="")
        print(f"{strike1.Name} : {strike1.Runs} {strike1.Bowls} {strike1.fours} {strike1.sixes} {strike1.Runrate}")
        if strike==strike2:
            print("*",end="")
        print(f"{strike2.Name} : {strike2.Runs} {strike2.Bowls} {strike2.fours} {strike2.sixes} {strike2.Runrate}")
        print(f"CRR : {crr}  RRR : {rrr}")
        if (target-totalruns)>0:
            print(f"{target-totalruns} runs required in {(overs*6)-((over*6)+j)} balls")
        print(f"{strikeb.Name} : {strikeb.Wickets}/{strikeb.RunOvr}({strikeb.Overs}.{j})")
        print(Outp)
if win==False:
    if totalruns>target:
        print(f"{Inn2} Wins by {10-wickets} Wickets!")
    elif totalruns==target:
        print(f"Match is Tie!")
    else:
        print(f"{Inn1} Wins by {target-totalruns} Runs!")
prstat=""
while prstat!='P':
    prstat=PrintStat()
    if prstat!='P':
        print("Invalid Input!")
print(f"{Inn1}")
print(f"{target}/{Fwickets}")
print(f"{Fover}.{Fball}")
print(f"{Inn2}")
print(f"{totalruns}/{wickets}")
print(f"{over}.{j}")
print(f"{Inn1} Stats : ")
print(f"             R   B   4s  6s  S/R")
for i in range(0,11):
    if Inn1==firstTeam:
        print(f"{Players1[i].Name} : {Players1[i].Runs} {Players1[i].Bowls} {Players1[i].fours} {Players1[i].sixes} {Players1[i].Runrate}")
        print(f"{Players1[i].Out}")
    else:
        print(f"{Players2[i].Name} : {Players2[i].Runs} {Players2[i].Bowls} {Players2[i].fours} {Players2[i].sixes} {Players2[i].Runrate}")
        print(f"{Players2[i].Out}")
print("              O  R  W  E")
for i in range(0,11):
    if Inn1==firstTeam:
        print(f"{Players2[i].Name} : {Players2[i].Overs} {Players2[i].RunOvr} {Players2[i].Wickets} {Players2[i].Economy}")
    else:
        print(f"{Players1[i].Name} : {Players1[i].Overs} {Players1[i].RunOvr} {Players1[i].Wickets} {Players1[i].Economy}")
print(f"{Inn2} Stats : ")
print(f"             R   B   4s  6s  S/R")
for i in range(0,11):
    if Inn2==firstTeam:
        print(f"{Players1[i].Name} : {Players1[i].Runs} {Players1[i].Bowls} {Players1[i].fours} {Players1[i].sixes} {Players1[i].Runrate}")
        print(f"{Players1[i].Out}")
    else:
        print(f"{Players2[i].Name} : {Players2[i].Runs} {Players2[i].Bowls} {Players2[i].fours} {Players2[i].sixes} {Players2[i].Runrate}")
        print(f"{Players2[i].Out}")
print("              O  R  W  E")
for i in range(0,11):
    if Inn2==firstTeam:
        print(f"{Players2[i].Name} : {Players2[i].Overs} {Players2[i].RunOvr} {Players2[i].Wickets} {Players2[i].Economy}")
    else:
        print(f"{Players1[i].Name} : {Players1[i].Overs} {Players1[i].RunOvr} {Players1[i].Wickets} {Players1[i].Economy}")