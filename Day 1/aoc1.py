
def read_from_file():
    with open('day1data1.txt') as f:
        data = f.read()
        return data

# Don't worry about above
#############################


def solve(numbers):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(i+2, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return str(numbers[i]) + ' ' + str(numbers[j]) + ' ' + str(numbers[k]) + ' ' + str(numbers[i] * numbers[j] * numbers[k])
                else:
                    pass

############################
# Don't worry about below

str_data = read_from_file().split('\n')
test_data = [int(i) for i in str_data]
print(solve(test_data))

