import numpy as np

chunk_size = 10**6
total = 10**8

with open("hashing/n.txt", "w") as f:
    for _ in range(total // chunk_size):
        arr = np.random.randint(0, 11, chunk_size, dtype=np.int8)
        for num in arr:
            f.write(f"{num}\n")

print("File created successfully")