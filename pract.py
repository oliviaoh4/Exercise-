articles=['a', 'an', 'the']
sentence=["The cat in the hat"]
for line in sentence:
    line = line.lower()
    line=line.split(" ")
    ls=[]
    for word in line:
        if word not in articles:
            ls.append(word)
    total=" "
    for word in ls:
        total=total+" "+word
    print(total)
