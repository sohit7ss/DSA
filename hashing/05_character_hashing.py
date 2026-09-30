n = "abcaacdgxyzaazzcguhhjsaABAXCCAMNACZ"
m = ["a", "b", "z", "u", "v", "m", "A", "C"]


hash_list = [0]*58
for cha in n:
    ascii = ord(cha)
    index = ascii - 65
    hash_list[index] += 1
for cha in m:
    index = ord(cha) - 65
    print(f"{cha} : {hash_list[index]}")

print(hash_list)


# TC = O(n + m)
# SC = O(58) = O(1)