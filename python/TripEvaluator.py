def main():
    distance = 0
    ferry = 0
    gooddata = False
    while (gooddata == False):
        distance = int(input("How far you want to go: "))
        ferry = int(input("how much does the ferry cost? (if there is no cost, or there is no ferry, input 0): "))

        if distance < 0 or ferry < 0:
            print("invalid input. please enter a positive numberfor each field.")
        else:
            gooddata = True

    tripEvaluator(distance, ferry)

def tripEvaluator(distance, ferry):
    travel = [carCalc(distance,ferry), planeCalc(distance), trainCalc(distance)]
    cost = [0, 0, 0]
    time = [0, 0, 0]
    score = [0, 0, 0]

    
    for i in range(3):
        cost[i] = travel[i][0]
        time[i] = travel[i][1]
        score[i] = cost[i]+time[i]
        

    if score[0] < score[1] and score[0] < score[2]:
        dtime = decimalTimeConvert(time[0])
        print(f"you should take the car. it will cost ${cost[0]}, and will take {dtime[0]} hours and {dtime[1]} minutes.")
    elif score[1] < score[0] and score[1] < score[2]:
        dtime = decimalTimeConvert(time[1])
        print(f"you should take the plane. it will cost${cost[1]}, and will take {dtime[0]} hours and {dtime[1]} minutes.")
    else:
        dtime = decimalTimeConvert(time[2])
        print(f"you should take the train. it will cost ${cost[2]}, and will take {dtime[0]} hours and {dtime[1]} minutes.")
    
def carCalc(distance, ferry):
    cost = (distance*0.4)+ferry
    time = distance/100
    list = [cost, time]
    return list

def planeCalc(distance):
    cost = (distance*0.2)+200
    time = (distance/900)+3
    list = [cost, time]
    return list

def trainCalc(distance):
    cost = distance*0.25
    time = (distance/350)+0.5
    list = [cost, time]
    return list

def decimalTimeConvert(time):
    dtime = time%(1)
    time -= dtime
    dtime = (dtime*60)/100
    time += dtime
    hours = int(time)
    minutes = int((time%(1))*100)
    list = [hours, minutes]
    return list

main()