# Alif Islam
# Sunday, November 18, 2018

import random

# function    :  getParticipants
# input       :  none
# output      :  list participants, list participants2
# description :  get user input and add to a list of participants
def getParticipants():
    participants  = []
    participants2 = []

    print("Please enter the text file name (with extension) to extract the participant list from.")
    p = input('> ')

    oldFile = open(p, 'r+')

    # extract each participant from the text file and add to the list participants
    for line in oldFile:
        # strip the newline character from each participant
        participants.append(line.rstrip())
        participants2.append(line.rstrip())

    return participants, participants2

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
def generatePairs(giver, receiver, file):

    pairs = {}

    # randomize the list of people and the group
    random.shuffle(giver)
    random.shuffle(receiver)

    # iterate over each person
    for g in giver:
        for r in receiver:
            # check if p is being assigned to themselves and check if people[i]
            # has already been assigned to someone else
            if r != g:
                if r not in pairs.values():
                    pairs[g] = r

        writeToFile(g, pairs[g], file)

def main():
    participants, participants2 = getParticipants()

    newFile = open('SecretSanta.txt', 'w+')
    generatePairs(participants, participants2, newFile)
    newFile.close()

main()
