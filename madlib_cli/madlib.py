import re


def read_template(file = 'assets/make_me_a_video_game_template.txt'):
    try:
        print('Locating file')
    except FileNotFoundError:
        print('Could not find file')
    with open(file) as f:
        contents = f.read()
        return contents


arr = []


def parse_template(sample = read_template()):
    pattern = r"[{}]"
    pArr = []
    strList = re.split(pattern,sample)
    for str in strList:
        if 'adjective' in str.lower():
            arr.append(str)
            pArr.append('{}')
        elif 'noun' in str.lower():
            arr.append(str)
            pArr.append('{}')
        elif 'a first name' in str.lower():
            arr.append(str)
            pArr.append('{}')
        elif 'past tense verb' in str.lower():
            arr.append(str)
            pArr.append('{}')
        elif 'animal' in str.lower():
            arr.append(str)
            pArr.append('{}')
        elif 'a girl\'s name' in str.lower():
            arr.append(str)
            pArr.append('{}')
        elif 'number' in str.lower():
            arr.append(str)
            pArr.append('{}')
        else:
            pArr.append(str)
    return [("".join(pArr)), (tuple(arr))]


def merge(text,filler):
    text = text.format(*filler)
    return text

def userInput():
    templst = []
    for a in arr:
        response = input('Give me a(n) ' + a + ': ')
        templst.append(response)
    return templst


if __name__ == '__main__':
    print(merge(parse_template()[0],userInput()))
