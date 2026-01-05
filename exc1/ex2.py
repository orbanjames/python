fnam = input("Enter file name: ")
if len(fnam) < 1 : fnam = "clown.txt"
hand = open(fnam)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

# print(di)

tmp = list()
for k, v in di.items():
    newt = (v,k)
    tmp.append(newt)

# print("Flipped",tmp)
tmp = sorted(tmp, reverse=True)
# print('sorted',tmp[:5])

for v,k in tmp[:5] :
    print(k,v)
        