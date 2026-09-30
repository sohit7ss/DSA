def read(file):
    with open(file, "r") as w:
        data = w.read()
    return list(map(int, data.replace(" ", "").split(",")))


m = read("hashing/m.txt")
n = read("hashing/n.txt")


d = {}
for num in n:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1


for num in m:
    if num in d:
        print(f"{num} : {d[num]}")
    else:
        print(f"{num} : 1")
        


# print(d)

# it is more optimL way to for in n is any number not in between o to 10 then this work properly 
# TC  = O(m + n)
# SC = O()

