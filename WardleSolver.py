fi=open("SpellBeeInputfile.txt", "r")
fr= list(fi.read().split())
discard=list()
inword=list()
correct={x:[] for x in range(5)}
wrongplace={x:[] for x in range(5)}

for k in range(6):
    print(" _ -> white/black , * -> yellow , + -> green")
    letters=input()
    letters=letters.upper()
    pattern=input()
    for j in range(len(pattern)):
        if pattern[j]=='_':
            discard.append(letters[j])
        elif pattern[j]=='*':
            inword.append(letters[j])
            wrongplace[j].append(letters[j])
        elif pattern[j]=='+':
            if letters[j] in discard:
                discard.remove(letters[j])
            inword.append(letters[j])
            correct[j]=letters[j]
    discard=list(set(discard))
    inword=list(set(inword))

    for i in fr:
        i = i.upper()
        if len(i) != 5:
            continue
        else:
            word = set([x for x in i])

            if word - set(discard) != word:
                continue
            elif set(inword)-word:
                continue
            else:
                flag=True
                # print(i,correct)
                for j in range(5):
                    if ( correct[j] and correct[j]!= i[j] ) or ( i[j] in wrongplace[j] ) :
                        flag=False
                        break
                if flag:
                    print(i)


    # print(discard,inword,correct)
