import gc
import functools
import operator
import itertools
import time

path = open("input3.txt", "r").readlines()
wire1 = path[0].split(",")
wire2 = path[1].split(",")
"""
coordinates (x,y) = step[0,1]
        |(y -> step[1]) => (+)U; (-)D
        |
  ------|----- (x -> step[0]) => (+)R; (-)L
        |
        |

"""
"""
Solution is extremely inefficent and follows O(N^2) complexity with the largest issue surrounding how large was a 
single step that was taken. 
"""

start1 = time.time()
"""
-- PART1 SOLUTION: 
"""
def gobalCoordinates(wirePath):
    wirePosition = [0, 0]
    gc.collect()
    coordinates = []
    for step in wirePath:
        if step[0] == 'R':
            coordinates.append(list([wirePosition[0]+i,wirePosition[1]] for i in range(int(step[1:])+1)))
            wirePosition[0] += int(step[1:])
        elif step[0] == 'D':
            coordinates.append(list([wirePosition[0], wirePosition[1]-i] for i in range(int(step[1:])+1)))
            wirePosition[1] -= int(step[1:])
        elif step[0] == 'L':
            coordinates.append(list([wirePosition[0]-i, wirePosition[1]] for i in range(int(step[1:])+1)))
            wirePosition[0] -= int(step[1:])
        elif step[0] == 'U':
            coordinates.append(list([wirePosition[0], wirePosition[1]+i] for i in range(int(step[1:])+1)))
            wirePosition[1] += int(step[1:])
    return(coordinates)


g= gobalCoordinates(wire1)
g2= gobalCoordinates(wire2)
end1 = time.time()
# Code from <https://www.educative.io/edpresso/how-to-flatten-a-list-of-lists-in-python>
coordinatesW1 = functools.reduce(operator.iconcat, g, [])
coordinatesW2 = functools.reduce(operator.iconcat, g2, [])
#print(coordinatesW1)
#print(coordinatesW2)

# removing duplicates
coordinatesW1 = list(k for k,_ in itertools.groupby(coordinatesW1))
coordinatesW2 = list(k for k,_ in itertools.groupby(coordinatesW2))


# Code from <https://stackoverflow.com/questions/30911309/common-elements-between-two-lists-of-lists-intersection-of-nested-lists>
nt1 = map(tuple, coordinatesW1)
nt2 = map(tuple, coordinatesW2)

st1 = set(nt1)
st2 = set(nt2)

crosssec = map(list, st1.intersection(st2))

start2 = time.time()
dist = 99999
minsteps = 9999999999999999999
for w1 in st1.intersection(st2):
    w1 = list(w1)
    if w1 != [0, 0]:
        t = coordinatesW2.index(w1) + coordinatesW1.index(w1)
        print(f'FOUND CROSSECTION: {w1}')
        #print(abs(w1[0])+abs(w1[1]))
        minsteps = min(t, minsteps)
        dist = min(abs(w1[0])+abs(w1[1]),dist)
end2 = time.time()

"""
start3 = time.time()
dist = 99999
minsteps = 99999999999999999999999999999999999
for w in set(coordinatesW1).intersection(coordinatesW2):
    #if w1 in coordinatesW2 and w1 != [0,0]:
    print(f'FOUND CROSSECTION: {w}')
    #print(abs(w1[0])+abs(w1[1]))
    minsteps = min(coordinatesW1.index(w)+coordinatesW2.index(w), minsteps)
    dist = min(abs(w1[0])+abs(w1[1]),dist)
end3 = time.time()"""


print("------------ RESULTS -----------------")
print(f'SHORTEST INTERSECTING DISTANCE: {dist}')
print(f'SHORTEST STEPS TO INTERSECTING DISTANCE FROM THE GIVEN PATH: {minsteps}')
print(f'TRIAL1 STATS: {end1-start1}')
print(f'TRIAL2 STATS: {end2-start2}')
#print(f'TRIAL3 STATS: {end3-start3}')