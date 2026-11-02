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
        first_nume=float(first_num)
    
        exercise.append(first_num)
        print(exercise)





        plt.bar(exercise,first_num)
        plt.ylabel("Hours")
        plt.title("Students Exercise")
        plt.show()


