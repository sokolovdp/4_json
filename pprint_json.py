import json
import codecs
import sys


def load_data(filename):
    try:
        json_data = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    except json.decoder.JSONDecodeError:
        print("invalid json format")
        exit(1)
    else:
        return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


def main(filename):
    pretty_print_json(load_data(filename))


if __name__ == '__main__':
    main(sys.argv[1:][0])
