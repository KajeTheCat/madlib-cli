
def read_template(file):
    try:
        print('Locating file')
    except FileNotFoundError:
        print('Could not find file')
    with open(file) as f:
        contents = f.read()
        return contents
    


def parse_template(sample):
    sample.split(' ')



def merge(text,filler):
    text = text.format(*filler)
    return text


if __name__ == '__main__':
    read_template()
    parse_template()
    merge()
