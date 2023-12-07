

def process_revelation(revelation):
    revelation = revelation.split(";")
    for cubes in revelation:
        cubes = cubes.split(",")
        for tup in cubes:
            n, color = tup.strip().split(" ")
            n = int(n)
            if (color == 'red' and n > 12)\
                or (color == 'blue' and n > 14)\
                or (color == 'green' and n > 13):
                return False
    return True

def test():
    assert process_revelation("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert process_revelation("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert not process_revelation("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert not process_revelation("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    assert process_revelation("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")

# test()

f = open("../infiles/input-02a.txt", "r")
data = f.readlines()
f.close()

sum = 0
for line in data:
    line = line.strip()
    game, revelation = line.split(":")
    id = int(game.split(" ")[1])
    
    if process_revelation(revelation):
        print(id)
        sum += id

print(sum)