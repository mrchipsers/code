import random
def lightbulb():
    count=0
    light=False
    people = []
    while True:
        person = random.randint(0,100)
        if person==1 and light==True:
            if count==100:
                return people
            count+=1
            light = False
        else:
            if person not in people:
                light=True
                people.append(person)

def check():
    people = lightbulb()
    for i in range(100):
        if i not in people:
            return False
    return True

print(check())
            
            