T = int(input())

for _ in range(T):
    N = int(input())

    type1 = set()
    type2 = set()
    for _ in range(N):
        clothes = input().strip().split()
        type1.add(clothes[0])
        type2.add(clothes[1])

    print(len(type1) * len(type2))

"""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face

5
3
"""
