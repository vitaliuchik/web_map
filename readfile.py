import json


def str_between(string, ch1, ch2):
    result_str = ''
    for i, symbol in enumerate(string):
        if symbol == ch1:
            string = string[i+1:]
            break
    for i, symbol in enumerate(string):
        if symbol == ch2:
            string = string[:i]
            break
    result_str = string
    return result_str


def cut_address(address):
    address = address.split(',')
    if len(address) > 2:
        address = address[-2:]
    return ','.join(address).strip()


file = open('locations.list', encoding='latin-1')
lines = file.readlines()[14:]
file.close()


movies = dict()
addresses = set()
for line in lines[:-1]:
    if '\"' in line:
        name = str_between(line, '\"', '\"')
    else:
        name = line[:line.index('(')].strip()
    year = str_between(line, '(', ')')
    line = line[line.index(')')+1:]
    if '}' in line:
        line = line[line.index('}') + 1:]
    if '(' in line:
        line = line[:line.index('(')]
    address = cut_address(line.strip())
    addresses.add(address)
    movies[year] = movies.get(year, list())
    movies[year].append([name, address])

file = open('years.json', 'w')
file.write(json.dumps(movies))
file.close()

# створює файл з адресами міст та країн
# file = open('adresses.txt', 'w', encoding='latin-1')
# for lst in list(addresses):
#     print(lst, file=file)
# file.close()






