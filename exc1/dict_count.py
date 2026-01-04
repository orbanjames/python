fnam = input("Enter file name: ")
if len(fnam) < 1 : fnam = "clown.txt"
hand = open(fnam)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w, 'new', di[w])
       
print(di)