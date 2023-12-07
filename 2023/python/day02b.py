def process_revelation(revelation):
    minR = 0
    minB = 0
    minG = 0
 
    revelation = revelation.split(";")
    for cubes in revelation:
        cubes = cubes.split(",")
        for tup in cubes:
            n, color = tup.strip().split(" ")
            n = int(n)
            if (color == 'red' and n > minR):
                minR = n
            if (color == 'blue' and n > minB):
                minB = n
            if (color == 'green' and n > minG):
                minG = n
    return minR * minG * minB

def test():
    assert process_revelation("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48
    assert process_revelation("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12
    assert process_revelation("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 1560
    assert process_revelation("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 630
    assert process_revelation("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36

# test()

f = open("../infiles/input-02b.txt", "r")
data = f.readlines()
f.close()

sum = 0
for line in data:
    line = line.strip()
    game, revelation = line.split(":")
    
    sum += process_revelation(revelation)

print(sum)