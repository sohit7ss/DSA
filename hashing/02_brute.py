def read(file):
    with open(file, "r") as r:
        data = r.read()
    return list(map(int, data.replace(" ", "").split(",")))

m = read("hashing/m.txt")
n = read("hashing/n.txt")

for num in m:
    count = 0
    for i in n:
        if i == num:
            count += 1
    print(count)

# here time complexity is O(m * n)
#  SC = O(1)