import random

def generatePairs(file):

    people = ['alif', 'sarah', 'shishir', 'pawel', 'ahmad', 'noah',
    'tubby', 'brandon', 'greg', 'bobby', 'kwong', 'niggest', 'cross', 'anthony']

    pairs = {}

    random.shuffle(people)

    for p in people:
        for i in range(len(people)):
            if p != people[i]:
                if people[i] not in pairs.values():
                    pairs[p] = people[i]
        newstr = p + ' will buy a gift for ' + pairs[p] + '\n'
        file.write(newstr)

    return pairs

def main():
    f = open('SecretSanta.txt', 'w+')
    generatePairs(f)
    f.close()

main()
