import random

# function    :  getParticipants
# input       :  none
# output      :  list participants
# description :  get user input and add to a list of participants
def getParticipants():
    participants = []

    print("Please enter the text file name (with extension) to extract the participant list from.")
    p = input('> ')

    oldFile = open(p, 'r+')

    # extract each participant from the text file and add to the list participants
    for line in oldFile:
        # strip the newline character from each participant
        participants.append(line.rstrip())

    return participants

# function    :  writeToFile
# input       :  str user1, str user1, file file
# output      :  none
# description :  write the names of user 1 and user2 to a given file
def writeToFile(user1, user2, file):
    newstr = user1 + ' will buy a gift for ' + user2 + '\n'
    file.write(newstr)

# function    :  generatePairs
# input       :  list people, file file
# output      :  none
# description :  generate secret Santa pairs
def generatePairs(people, file):

    pairs = {}

    # randomize the list of pe
    random.shuffle(people)

    # iterate over each person
    for p in people:
        for i in range(len(people)):
            # check if p is being assigned to themselves and check if people[i]
            # has already been assigned to someone else
            if people[i] != p and people[i] not in pairs.values():
                    pairs[p] = people[i]
        writeToFile(p, pairs[p], file)

def main():
    participants = getParticipants()

    newFile = open('SecretSanta2.txt', 'w+')
    generatePairs(participants, newFile)
    newFile.close()

main()
