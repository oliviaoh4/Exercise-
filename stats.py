import matplotlib.pyplot as plt
try:
    fhand=open("StudentExercise.csv")
except:
    print("File cannot be opened")
    exit()
next(fhand)
exercise=[]
for line in fhand:
    pieces=line.split(",")
    first_num=pieces[0]
    if first_num!='':
        first_num=float(first_num)
        exercise.append(first_num)
        print(exercise)
elms=(max(exercise))-(min(exercise))+1
amount=[0]*int(elms)
for time in exercise:
    nt=int(time-min(exercise))
    print(nt)
    amount[nt]+=1
    
values=list(range(int(min(exercise)),(int(max(exercise))+1)))


plt.bar(values,amount)
plt.ylabel("Hours")
plt.title("Students Exercise")
plt.show()


