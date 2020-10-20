"""
    PART2 - terminology:
        Instructional Pointers - he instruction pointer increases by the number of values in the instruction for this case => 1(opcode)+3(param)
        Address - A position in memory is called an address
        Memory - Intcode programs are given as a list of integers; these values are used as the initial state for the computer's memory

    CHALLENGE:
        determine what pair of inputs produces the output 19690720.

    address 1 -> noun
    address 2 -> verb
    Each of the two input values will be between 0 and 99, inclusive.

"""
import math as m
import gc

def ProgAlarm(Intcode):
    # Clear memory
    gc.collect()
    pos = 0
    while pos < len(Intcode) and Intcode[pos+3] < len(Intcode):
        if Intcode[pos] == 1:
            elem1 = Intcode[Intcode[pos+1]]
            elem2 = Intcode[Intcode[pos+2]]
            Intcode[Intcode[pos+3]] = elem1+elem2
            """print("elem1: ", elem1)
            print("elem2: ", elem2)
            print("gravityAssist[pos+2]: ", gravityAssist[pos+3])"""
        elif Intcode[pos] == 2:
            elem1 = Intcode[Intcode[pos + 1]]
            elem2 = Intcode[Intcode[pos + 2]]
            Intcode[Intcode[pos + 3]] = elem1 * elem2
        elif Intcode[pos] == 99:
            break
        pos += 4
    return Intcode

# BRUTE FORCE METHOD O(N^2) COMPLEXITY
"""
Order mattered for this challenge therefore, the range had to extend 0 - 100 for both the variables. 
"""
if __name__ == '__main__':
    count = 0
    rawCodetext = (open("input2.txt", "r").read()).split(",")
    rawCode = [int(val) for val in rawCodetext]
    for verb in range(0, 100):
        for noun in range(0, 100):
            rawCodetext[2] = verb
            rawCodetext[1] = noun
            rawCode = [int(val) for val in rawCodetext]
            if ProgAlarm(rawCode)[0] == 19690720:
                res = ProgAlarm(rawCode)
                print("WE FOUND IT! ")
                print((100 * noun) + verb)
                break

"""

if __name__ == '__main__':
    count = 0
    rawCodetext = (open("input2.txt", "r").read()).split(",")
    rawCode = [int(val) for val in rawCodetext]
    for position in range(0, 100):
        if ProgAlarm(rawCode)[0] <= 19690720:
            rawCodetext[2] = verb
            rawCodetext[1] = noun
        rawCode = [int(val) for val in rawCodetext]
        if ProgAlarm(rawCode)[0] == 19690720:
            res = ProgAlarm(rawCode)
            print("WE FOUND IT! ")
            print((100 * noun) + verb)
            break
"""

"""
noun = 0 
verb = 99
while (noun >=0) and (verb <=99):    
    if ProgAlarm(Intcode) > 19690720:
        #noun -= m.floor(noun/2)
        verb += m.floor(verb/2)
        Intcode[2] = verb
    elif ProgAlarm(Intcode) < 19690720:
        noun -= m.floor(noun / 2)
        Intcode[1] = noun
    elif ProgAlarm(Intcode) == 19690720:
        break"""



