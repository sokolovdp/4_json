import json
import codecs
import sys


def load_data(filename):
    try:
        json_data = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    except IOError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return json_data


def pretty_print_json(data):
    json_text = json.dumps(data, sort_keys=True, indent=3, ensure_ascii=False)
    print(json_text)


def main(filename):
    temp = load_data(filename)
    if temp:
        pretty_print_json(temp)
    else:
        print("json file {} read error".format(filename))

if __name__ == '__main__':
    main(sys.argv[1:][0])
