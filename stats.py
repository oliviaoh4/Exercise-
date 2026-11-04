import matplotlib.pyplot as plt
##try:
##    fhand=open("StudentExercise.csv")
##except:
##    print("File cannot be opened")
##    exit()
##next(fhand)
##exercise=[]
##for line in fhand:
##    pieces=line.split(",")
##    first_num=pieces[0]
##    if first_num!='':
##        first_num=float(first_num)
##        exercise.append(first_num)
##        print(exercise)
##elms=(max(exercise))-(min(exercise))+1
##amount=[0]*int(elms)
##for time in exercise:
##    nt=int(time-min(exercise))
##    print(nt)
##    amount[nt]+=1
##    
##values=list(range(int(min(exercise)),(int(max(exercise))+1)))
##
##
##plt.bar(values,amount)
##plt.ylabel("Hours")
##plt.title("Students Exercise")
##plt.show()


import numpy as np
data=np.genfromtxt("StudentExercise.csv", delimiter = ",", skip_header=1)
print(data[:,0])
nums=data[:,0]
avg=np.nanmean(nums)
print("average is {:.2f}".format(avg))

count=0
for num in nums:
    if num>avg:
        count+=1
print(count)
print(len(nums))
prop_above=(165/362)
print(prop_above)

print("percent above avg is {0:.0%}".format(prop_above))

median=np.nanmedian(nums)
print("Median is {0:.2f}".format(median))


