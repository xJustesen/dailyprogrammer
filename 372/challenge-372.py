def check_string(STR, ID):
    '''
    Given a string (STR) containing only lowercase letters (ID), this function finds whether every letter that appears in the string appears the same number of times.
    An empty list is handled as TRUE
    '''

    SIZE = len(ID)
    counts = [0] * SIZE

    # Count number of time a letter appears
    for i in range(SIZE):
        id = ID[i]
        for s in STR:
            if id == s:
                counts[i] += 1

    return len(set(counts)) <= 1


def output(STR, ID):
    ''' Writes output from "check_string" to terminal '''
    if check_string(STR, ID):
        print("The string: '" + STR + "' is balanced.")
    else:
        print("The string: '" + STR + "' is not balanced.")


def getLetters(STR):
    ''' Given a string (STR) containing only lowercase letters, this function returns a list of which lowercase letters (ID) appear in the string '''
    if len(STR) > 0:
        ID = [STR[0]]

        for s in STR:
            for id in ID:
                isUnique = False if s == id else True
                if isUnique == False:
                    break
            if isUnique:
                ID.append(s)
    else:
        ID = STR

    return ID


def main():

    balanced = "xxxyyy"
    notBalanced = "xxxyy"
    empty = ""
    single = "x"
    mixed = "aaaxxafxbcxhefqf"

    ID = getLetters(balanced)
    output(balanced, ID)
    ID = getLetters(notBalanced)
    output(notBalanced, ID)
    ID = getLetters(empty)
    output(empty, ID)
    ID = getLetters(single)
    output(single, ID)
    ID = getLetters(mixed)
    output(mixed, ID)


if __name__ == '__main__':
    main()
