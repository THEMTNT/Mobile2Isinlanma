import configparser

gamename = "metin2f-Win64-Shipping.exe"
offsetsx =[0x0405F5C8,0x138, 0x1E0]
offsetsy =[0x0405F5C8,0x138, 0x1E4]
offsetsz =[0x0405F5C8,0x138, 0x1E8]


def read_offsets_from_file():
    offsets = {'x': [], 'y': [], 'z': []}
    config = configparser.ConfigParser()
    config.read("offsets.ini")

    for key in offsets.keys():
        values = config.get('offsets', f'offsets{key}')
        offsets[key] = [int(value.strip(), 16) for value in values.split(',')]

    return offsets

