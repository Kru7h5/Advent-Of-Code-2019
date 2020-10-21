import time

count = 0
start = time.time()
for givenNumber in range(271973, 785961):
    valuesPossible = [int(i) for i in str(givenNumber)]
    pairWiseDifference = [valuesPossible[i]-valuesPossible[i+1] for i in range(len(valuesPossible)-1)]
    indices = [i for i, x in enumerate(pairWiseDifference) if x == 0]
    endloop = time.time()
    if all(i <= 0 for i in pairWiseDifference) and 0 in pairWiseDifference:
        count += 1
        #if pairWiseDifference.count((0)) > 1 and all(i == 1 for i in [indices[i] - indices[i + 1] for i in range(len(indices) - 1)]):

endfin = time.time()
print(count)
print(f'TIME FOR LOOP: {endloop-start}')
print(f'TIME FOR LOOP: {endfin-start}')