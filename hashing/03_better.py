def read(file):
    with open(file, "r") as r:
        data = r.read()
    return list(map(int, data.replace(" ", "").split(",")))

m = read("hashing/m.txt")
n = read("hashing/n.txt")


# hash in a list 

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1

for num in m:
    if num>10 or num<0:
        print(0)
    else:
        print(hash_list[num])