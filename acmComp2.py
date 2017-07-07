def main():
    numPeople = int(input())
    peopleLine = input()
    people = peopleLine.split()
    # print(people)
    groceries = input()
    # print(groceries)
    available = []
    while(len(groceries) != 0):
        here = groceries.find('1')
        notHere = groceries.find('0')
        if (here < notHere):
            available.append(groceries[:here-1])
            groceries = groceries[here+2:]
        else:
            groceries = groceries[notHere+2:]
    indexInc = len(available)
    for i, person in enumerate(people):
        print(person, end=' ')
        for j in range(i,len(available),indexInc):
             print(available[j], end=' ')
        print()

            # if (i % len(people) == i):
            #     print(available[i])





    # for i in range(20):

main()
