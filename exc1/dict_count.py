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
       
# print(di) Only to see the dictionary

# find the most common word
# bigcount = None
# bigword = None
# for w,c in di.items():
#     if bigcount is None or c > bigcount:
#         bigword = w
#         bigcount = c
# print(bigword, bigcount)
# OR
largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k
print(theword, largest)

