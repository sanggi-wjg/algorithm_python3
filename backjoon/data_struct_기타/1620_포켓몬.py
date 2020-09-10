import sys

N, M = map(int, sys.stdin.readline().strip().split())

data = { }

for n in range(1, N + 1):
    name = sys.stdin.readline().strip()
    data.setdefault(str(n), name)
    data.setdefault(name, str(n))

for m in range(M):
    target = sys.stdin.readline().strip()
    sys.stdout.writelines(data.get(target) + '\n')

"""
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

Pikachu
26
Venusaur
16
14
"""
