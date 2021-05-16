def runLengthEncoding(string):
    counter = 0
    oldLetter = string[0]
    message = ''
    for letter in string:
        if letter == oldLetter:
            if counter == 9:
                message += '9' + oldLetter
                counter = 1
            else:
                counter += 1
        else:
            message += str(counter) + oldLetter
            oldLetter = letter
            counter = 1
    message = message + str(counter) + string[-1]
    return message
