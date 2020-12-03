def read_from_file():
    with open('Input test.txt') as f:
        data = f.read()
        data = data.split('\n')
        return data


def validate_password_olde(pwd):
    pwd = pwd.split(' ')
    NumofOcc = pwd[0].split('-')
    minnum = int(NumofOcc[0])
    maxnum = int(NumofOcc[1])
    Letter = pwd[1].replace(':', '')
    word = pwd[2]

    tally = 0
    for letter in word:
        if letter == Letter:
            tally = tally + 1

    if minnum <= tally <= maxnum:
        return True
    else:
        return False


def validate_password(pwd):
    pwd = pwd.split(' ')
    positions = pwd[0].split('-')
    first_position = int(positions[0]) - 1
    last_position = int(positions[1]) - 1
    letter = pwd[1].replace(':', '')
    word = pwd[2]

    tally = 0
    if word[first_position] == letter:
        tally = tally + 1
    if word[last_position] == letter:
        tally = tally + 1

    if tally == 1:
        return True
    else:
        return False

def read_from_elements(passwords):
    count = 0
    for password in passwords:
        is_valid = validate_password(password)
        if is_valid:
            count = count + 1
    return count


print(read_from_elements(read_from_file()))
